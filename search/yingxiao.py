#coding=utf-8
#内容制胜
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import common.CsvDataRead as cdr

FILE_PATH = "data.csv"

if __name__ == '__main__':
    dataRead = cdr.CsvDataRead(FILE_PATH)
    url = dataRead.get_url_from_data_file(10)

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()

#基本信息
#学习人姓名
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[1]/div[1]/input[1] ").send_keys("特训营")
#学习人联系方式
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[2]/div[1]/input[1] ").send_keys("13655554478")
#学习人年龄段
age= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[4]/div[1]/select[1] "))
age.select_by_index("1")
#学习人职位
zhiwei= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[3]/div[1]/select[1] "))
zhiwei.select_by_index("1")
#所在地区
shengfen= Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div/select[1]"))
shengfen.select_by_index("2")  # 通过index进行选择,index从0开始
sleep(2)
shengfen= Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div/select[2]"))
shengfen.select_by_index("2")  # 通过index进行选择,index从0开始
sleep(2)
#店铺地址
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div/input").send_keys("https://www.taobao.com/")
#店铺层级
cengji= Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[7]/div/select"))
cengji.select_by_index("1")
#您的店铺所属一级类目
leimu= Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[8]/div/select"))
leimu.select_by_index("2")
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[9]/div/div/div[1]/input").click()
sleep(2)
#您的店铺所属二级类目
driver.find_element_by_xpath("//*[@id='ui-select-choices-row-0-2']").click()
#开店时长
longtime=Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[10]/div/select"))
longtime.select_by_index("2")
#电商团队人数
peoplenum=Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[11]/div/select"))
peoplenum.select_by_index("2")
# 团队构成
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[12]/div/p/label[1]/input").click()
#店铺年销售额
#driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[9]/div/div").send_keys("1")
driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[13]/div/input").send_keys("10000")
#您的微淘等级是？
age=Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[14]/div/select"))
age.select_by_index("1")
#店铺粉丝数
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[15]/div/input").send_keys("10")
#其他渠道粉丝数
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[16]/div[2]/div[1]/input").send_keys("10")
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[16]/div[2]/div[2]/input").send_keys("100")
#您跟达人合作过什么渠道？
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[19]/div/p/label[1]/input").click()
#您对内容营销最大的困惑是什么？
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[20]/div/textarea").send_keys("客服现状")
#问题一
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[21]/div[2]/div[1]/textarea").send_keys("客服现状")
#问题二
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[21]/div[2]/div[2]/textarea").send_keys("客服现状")
#问题三
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[21]/div[2]/div[3]/textarea").send_keys("客服现状")
#点击保存
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/div[22]/button").click()
sleep(3)
#driver.quit()
