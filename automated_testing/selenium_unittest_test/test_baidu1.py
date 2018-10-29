#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: selenium_unittest_test.py
#
# Selenium和unittest结合的测试脚本
# Selenium常用API

__author__ = 'genghui'

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By

# 利用 Keys 这个类来模拟键盘输入
from selenium.webdriver.common.keys import Keys
# 下拉选项卡类
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class SearchTest(unittest.TestCase):
    # 用于初始化
    def setUp(self):
        self.driver = webdriver.Chrome()              # 打开chrome

        # Firefox驱动
        #profile = webdriver.FirefoxProfile()          # Firefox配置管理器(ProfileManager)
        #profile.native_events_enabled = True          # 本地事件
        #self.driver = webdriver.Firefox(profile)

        # IE驱动
        #self.driver = webdriver.Ie()

        #


        self.driver.maximize_window()                 # 最大化浏览器窗口
        self.driver.implicitly_wait(20)               # 设置隐式时间等待
        self.base_url = "https://www.baidu.com"       # 设置访问的url
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_search(self):
        """
        百度首页搜索
        """
        driver = self.driver
        driver.get(self.base_url + "/")               # 地址栏输入百度地址,打开请求的URL
        url0 = driver.current_url
        title0 = driver.title

        # 显式等待5秒
        wait = WebDriverWait(driver, 5)

        #driver.find_element_by_id("kw").click()
        #driver.find_element_by_name("wd").click()
        #driver.find_elements_by_class_name("s_ipt")

        driver.find_element_by_class_name("s_ipt").click()
        driver.find_element_by_id("kw").clear()                     # clear(),清除输入的文本
        #driver.find_element_by_id("kw").send_keys("Selenium3")     # send_keys(),向文本输入内容
        #同样你还可以利用Keys这个类来模拟点击某个按键
        #element.send_keys("and some", Keys.ARROW_DOWN)


        # 通过查找元素的路径去查找元素
        #driver.find_element_by_xpath('//*[@id="kw"]').send_keys("Selenium3")
        # 通过对页面中的CSS元素定位
        driver.find_element_by_css_selector("#kw").send_keys("Selenium")            # 搜索输入框输入Selenium3


        #driver.find_element_by_id("su").click()
        #button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="su"]')))   # 确认元素是否是可点击的                                                                 # 等待3秒
        driver.find_element_by_xpath('//*[@id="su"]').click()                          # 点击百度一下按钮

        # 第一种写法
        # 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表
        #driver.find_element_by_xpath('//*[@id="1"]/h3/a/em[text()="Selenium"]').is_displayed()    # 判断我们的目标元素是否在页面显示
        # print("hello world")

        # 第二种写法
        element_string = driver.find_element_by_xpath('//*[@id="1"]/h3/a').text
        if element_string == u"Selenium - Web Browser Automation":
            print("测试成功, 结果和预期结果匹配")



    def test_login(self):
        """
        百度登录
        """
        driver = self.driver
        driver.get(self.base_url + "/")

        # 打印页面源代码
        #print(driver.page_source)

        #driver.find_element_by_link_text("登录").click()
        driver.find_element_by_partial_link_text("使用").click()
        driver.find_element_by_link_text("百度首页").click()

        time.sleep(2)
        print("baidu login")


    def test_01baidu_setting(self):
        """ 百度首页设置 """
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(2)

        driver.find_element_by_css_selector("div#u1 a.pf").click()
        driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()

        # 用selenium做自动化，有时候会遇到需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽、下拉菜单等等。而selenium给我们提供了一个类来处理这类事件——ActionChains
        # 此处下拉菜单就需要模拟, 使用perform()执行action
        # 将动作附加到动作链中串行执行。当你调用ActionChains的方法时，不会立即执行，而是会将所有的操作按顺序存放在一个队列里，当你调用perform()方法时，队列中的时间会依次执行
        time.sleep(2)
        ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, "#gxszButton > a.prefpanelgo")).perform()
        # 通过switch_to.alert获取弹窗对象
        driver.switch_to.alert.accept()

        time.sleep(3)
        print("test_baidu__test_01baidu_setting")

        # frame中实际上是嵌入了另一个页面，而webdriver每次只能在一个页面识别，因此需要先定位到相应的frame，对那个页面里的元素进行定位
        # 如果iframe有name或id的话，直接使用switch_to.frame("name值")或switch_to.frame("id值") (driver.switch_to_frame()已不建议使用)
        #driver.switch_to_frame()
        #driver.switch_to.frame('***')   # 需先跳转到iframe框架

        # 跳回原页面
        #driver.switch_to.parent_frame()
        #driver.switch_to.default_content()

        # 不在当前视图范围内的元素的操作
        # 执行Javascript, 可以直接调用js方法来实现一些操作
        #driver.execute_script("window.scrollBy(0, 200)", "")   # 页面向下滚动200px
        #driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "")   # 向下滚动至页面底部
        # 可以执行任意javascript来找到一个元素，只要你返回一个DOM元素,它将自动转换为一个WebElement对象
        #ele = driver.execute_script("return $('.cheese')[0]")        # 页面加载了jQuery


    def test_ele_operation(self):
        """ 测试元素交互操作 """
        driver = self.driver
        url = "http://www.zhihu.com/explore"
        driver.get(url)


        # cookie操作

        print(driver.get_cookies())            # 获得所有的cookie
        driver.add_cookie({'name': 'genghui', 'domain': 'www.zhihu.com', 'value': 'hello selenium'})
        print(driver.get_cookies())
        driver.delete_cookie('domain')
        print(driver.get_cookies())
        driver.delete_all_cookies()
        print(driver.get_cookies())


        #time.sleep(2)
        #input = driver.find_element_by_class_name("zu-top-add-question")

        # 显式等待5秒
        wait = WebDriverWait(driver, 5)
        input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "zu-top-add-question")))    # 确认元素是否已经出现了
        logo = driver.find_element_by_id("zh-top-link-logo")

        print(logo.get_attribute("class"))        # 获取元素属性
        print(input.text)                         # 获取文本值
        print(input.id)
        print(input.location)
        print(input.tag_name)
        print(input.size)
        print(input.size)

        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.execute_script("alert('To Bottom')")

        # 浏览器的前进和后退
        #driver.forward()
        #driver.back()


        # 元素拖拽操作
        #source_ele = driver.find_element_by_id('source')
        #target = driver.find_element_by_id('target')

        #action_chains = ActionChains(driver)
        # 拖拽，拖拽使用时注意加等待时间，有时会因为速度太快而失败
        #action_chains.drag_and_drop(source_ele, target).perform()

        # 模拟键盘按键操作
        #action_chains.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()          # 模拟ctrl + c
        #action_chains.key_down(Keys.CONTROL, input).send_keys('v').key_up(Keys.CONTROL).perform()   # 模拟ctrl + v
        # 复制粘贴用WebElement< input >.send_keys()也能实现




        # 表单

        # 表单下拉列表(select标签)
        # 1、通常的处理方法
        #ele = driver.find_element_by_xpath("//select[@name='name']")
        #all_options = ele.find_elements_by_tag_name('option')
        #for option in all_options:
        #    print("Value is: %s " % option.get_attribute('value'))
        #    option.click()

        # 2、webdriver的处理方法
        #select_ele = Select(driver.find_element_by_xpath("//select[@name='name']"))
        #select_ele.select_by_index(index)                                              # 根据索引来选择
        #select_ele.select_by_visible_text('***')                                       # 根据文字来选择
        #select_ele.select_by_value('***')                                              # 根据value来选择
        # 全部取消选择
        #select_ele.deselect_all()
        # 获取所有的已选选项
        #all_selected_options = select_ele.all_selected_options
        # 获取所有可选选项
        #normal_options = select_ele.options

        # 表单提交
        #driver.find_element_by_id("submit").click()
        # 单独提交某一元素,WebDriver 会在表单中寻找它所在的表单，如果发现这个元素并没有被表单所包围，那么程序会抛出NoSuchElementException的异常
        #select_ele.submit()

        time.sleep(2)
        print("success")


    def test_tabs_operation(self):
        """ 选项卡(标签页/页面)管理 """
        driver = self.driver

        driver.get("https://www.baidu.com")

        time.sleep(2)
        driver.execute_script("window.open()")    # 新开选项卡
        print(driver.window_handles)              # 不同的选项卡列表,获取每个窗口的操作对象

        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])     # 切换至第2个选项卡
        driver.get("https://www.taobao.com")

        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])     # 切换至第1个选项卡
        driver.get("https://python.org")

        print('tabs manage')


    def test_exception_operation(self):
        """ 异常处理 """
        driver = self.driver
        try:
            driver.get("https://www.google.com")
        except TimeoutException:
            print('Time Out')



        try:
            driver.find_element_by_id("hello")
        except NoSuchElementException:
            print('No Element')
        finally:
            print('Done')


        # HtmlUnit 驱动

        #driver = webdriver.Remote("http://****", webdriver.DesiredCapabilities.HTMLUNIT)
        # 启用JavaScript
        #driver = webdriver.Remote("http://***", webdriver.DesiredCapabilities.HTMLUNITWITHJS)





    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False

        return True


    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False

        return True


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def tearDown(self):
        #self.driver.close()
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    # 执行方法的默认顺序是：根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z
    unittest.main()