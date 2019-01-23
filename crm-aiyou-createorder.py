#coding=utf-8
#爱柚-新建订单-现销
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://10.64.83.134/txws_crm/admin/login.html")

driver.find_element_by_id("account").send_keys("陈琳")
driver.find_element_by_id("password").send_keys("123456")
driver.implicitly_wait(10)

#点击登录
driver.find_element_by_class_name("btn-login").click()
driver.implicitly_wait(3)
# 浏览器窗口最大化
driver.maximize_window()
#点击业务中心
driver.find_element_by_class_name("menu-nav").click()
#点击我的客户
driver.find_element_by_class_name("icon-khgl").click()
driver.implicitly_wait(3)

handle = driver.current_window_handle
print ("首句柄",handle)
#点击第一条数据
driver.find_element_by_xpath("//*[@id='uiViews']/div[1]/div[2]/table/tbody/tr[3]/td[3]").click()
driver.implicitly_wait(5)

#点击订单信息按钮
#切换窗口之获取句柄
all_handle = driver.window_handles
print ("所有句柄",all_handle)
'''判断是否是首句柄，切换到新打开的页面'''
for i in all_handle:
    if i != handle:
        driver.switch_to_window(i)
        print (driver.title)    #打印页面title
#点击订单信息
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="uiViews"]/div[1]/div[1]/ul/li[4]').click()



#点击新建订单按钮
driver.find_element_by_xpath("//*[@id='uiViews']/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[2]/button").click()
driver.implicitly_wait(3)

#选择产品
chanpin=Select(driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[1]/div[2]/div/div/form/div[1]/p[2]/span[2]/select"))
chanpin.select_by_index("1")  # 通过index进行选择,index从0开始
#输入价格
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[1]/div[2]/div/div/form/div[1]/p[3]/span[2]/input ").send_keys("12000")
#输入数量
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[1]/div[2]/div/div/form/div[1]/p[4]/span[2]/input ").send_keys("2")
#点击下一步
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[1]/div[3]/button[1]").click()
driver.implicitly_wait(3)


#点击个人签约
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[2]/div[1]/ul/li[2]").click()
#签约信息
#签约人
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[2]/div[2]/div/form/div[1]/p[1]/span[2]/input ").send_keys("cxt")
#身份证号码
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[2]/div[2]/div/form/div[1]/p[2]/span[2]/input ").send_keys("622301111111111111")
#联系方式
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[2]/div[2]/div/form/div[1]/p[3]/span[2]/input ").send_keys("17822223333")
#订单信息
#订单类型
qianyueleixing=Select(driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[2]/div[2]/div/form/p[3]/span[2]/select"))
qianyueleixing.select_by_index("1")
#签约类型
qianyueleixing=Select(driver.find_element_by_xpath("//*[@id='uiViews']/div/div[1]/div[2]/div[2]/div/form/p[4]/span[2]/select"))
qianyueleixing.select_by_index("1")  # 通过index进行选择,index从0开始
#营收类型
driver.find_element_by_xpath('//*[@id="uiViews"]/div/div[1]/div[2]/div[2]/div/form/p[5]/span[2]/div/ul/li').click()
driver.find_element_by_xpath('//*[@id="uiViews"]/div/div[1]/div[2]/div[2]/div/form/p[5]/span[2]/div/div/ul/li/ul/li[1]/div').click()
#到单日期
driver.find_element_by_id('table-data').click()
#切换iframe页面
iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to_frame(iframe)
#点击今天
driver.find_element_by_id("dpTodayInput").click()
#退出iframe页面，返回主页面
driver.switch_to_default_content()
#点击下一步
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="uiViews"]/div/div[1]/div[2]/div[3]/button[2]').click()
#订单确认页面
#点击确定按钮
driver.find_element_by_xpath("//*[@id='uiViews']/div/div[2]/div/div[2]/div/div[3]/button").click()

driver.quit()
















