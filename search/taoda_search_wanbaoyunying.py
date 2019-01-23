#coding=utf-8
#淘大-玩爆运营

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import  sleep
import common.CsvDataRead as cdr

FILE_PATH = "data.csv"

if __name__ == '__main__':
    dataRead = cdr.CsvDataRead(FILE_PATH)
    url = dataRead.get_url_from_data_file(4)

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

#基本信息
#拍下订单时间
#driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1] ").send_keys("2017-08-16")
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/input").send_keys("2017-08-16")
#排课id
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div/input").send_keys("cxt")
# 拍课订单编号
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[3]/div/input").send_keys("cxt")
#拍单预留手机号
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div/input").send_keys("18078910000")
#您的名字
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[5]/div/input").send_keys("cxt")
#您的电话
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[6]/div/input").send_keys("18078910000")
#【重要】开通店铺公司（与开通店铺一一对应）
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[8]/div/input").send_keys("cxt")
#开通所在店铺预留联系人名字（淘宝或天猫）
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[9]/div/input").send_keys("cxt")
#开通所在店铺预留的联系人电话
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[10]/div/input").send_keys("18000000000")
#开通所在店铺预留邮箱
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[11]/div/input").send_keys("123@qq.com")
#【重要】店铺对接人旺旺（开通服务之后有专人联系此号）
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[12]/div/input").send_keys("1")
#您所在的城市是
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[13]/div/select[1]"))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[13]/div/select[2]"))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#开通店铺所属类目
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[14]/div/select"))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#您的电商团队人数
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[15]/div/select"))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#您的店铺层级---------
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[16]/div/select"))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#您的店铺人员架构组成---------
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[17]/div/p/label[1]/input").click()
#您目前最感兴趣的话题是
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[18]/div/p/label[1]/input").click()
#请您描述一下店铺的现状与需求
driver.find_element_by_xpath(".//*[@id='jingyinghui']/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[19]/div/textarea").send_keys("1")



driver.implicitly_wait(10)
#点击保存
driver.find_element_by_xpath("//button[@class='submitform margin_l349'] ").click()

#driver.quit()





