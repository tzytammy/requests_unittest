#coding=utf-8
#特训营-运营班
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import common.CsvDataRead as cdr

FILE_PATH = "data.csv"

if __name__ == '__main__':
    dataRead = cdr.CsvDataRead(FILE_PATH)
    url = dataRead.get_url_from_data_file(9)

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

#报名人信息
#报名人姓名
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/input ").send_keys("cxt")
#报名人联系方式
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/input ").send_keys("18078910000")
#报名人职位
baomingrenzhiwei= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[2]/div[3]/div/select "))
baomingrenzhiwei.select_by_index("1")
#报名人年龄段
baomingrenzhiwei= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[2]/div[4]/div/select "))
baomingrenzhiwei.select_by_index("1")


#店铺基本信息
#店铺类目
baomingrenzhiwei= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div/select"))
baomingrenzhiwei.select_by_index("1")
#店铺链接
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[3]/div/input").send_keys("https://www.tmall.com/?ali_trackid=2:mm_26632360_8858797_53458628:1519801823_312_1406923368&clk1=44bc340cc275bed99c1169c8554e6e23&upsid=44bc340cc275bed99c1169c8554e6e23")
#选择省份
shengfen= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[4]/div/select[1]"))
shengfen.select_by_index("2")  # 通过index进行选择,index从0开始
sleep(3)
#选择城市
shengfen= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[4]/div/select[2]"))
shengfen.select_by_index("1")
#店铺层级
dianpucengji= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[5]/div/select "))
dianpucengji.select_by_index("1")
#近1年销售额
dianpucengji= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[6]/div/select "))
dianpucengji.select_by_index("1")
#开店时长
dianpucengji= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[7]/div/select "))
dianpucengji.select_by_index("1")
#电商团队人数
dianpucengji= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[8]/div/select "))
dianpucengji.select_by_index("1")
#团队构成
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[9]/div/p/label[1]/input ").click()
#其他电商渠道
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[10]/div/p/label[1]/input ").click()
#供应链情况
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[11]/div/p/label[1]/input ").click()
#店铺类型
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[12]/div/p/label[1]/input ").click()
#近30天无线访客数
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[13]/div/input").send_keys("10")
#您的微淘等级
dianpucengji= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[14]/div/select"))
dianpucengji.select_by_index("1")
#描述一下您的产品运营状况
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[19]/div/textarea").send_keys("10")
#除了这个主题还有哪些是您目前急需了解的？
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[4]/div[20]/div/p/label[1]/input ").click()
#点击下一步
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/button ").click()
#参加人信息
#参见人姓名
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[5]/div[2]/div[1]/div/input").send_keys("cxt")
#参加人联系方式
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[5]/div[2]/div[2]/div/input").send_keys("18000000000")
#参加人职位
zhiwei= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[5]/div[2]/div[3]/div/select"))
zhiwei.select_by_index("2")  # 通过index进行选择,index从0开始
#参加人年龄段
zhiwei= Select(driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/div[5]/div[2]/div[4]/div/select"))
zhiwei.select_by_index("2")  # 通过index进行选择,index从0开始

#点击保存
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div[1]/div/div/button[2] ").click()
sleep(3)
driver.quit()
