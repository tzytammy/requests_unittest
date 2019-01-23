#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import common.CsvDataRead as cdr

FILE_PATH = "data.csv"

if __name__ == '__main__':
    dataRead = cdr.CsvDataRead(FILE_PATH)
    url = dataRead.get_url_from_data_file(1)

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

#店铺基本信息
#经营年限
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[3]/div[1]/input[1] ").send_keys("2")
#店铺链接
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[4]/div[1]/input[1] ").send_keys("http://www.taobao.com")
#选择类目
# 实例化一个Select类的对象
leimu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[5]/div[1]/select[1] "))

# 下面三种方法用于选择"篮球运动员"
leimu.select_by_index("2")  # 通过index进行选择,index从0开始

#店铺名称
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[6]/div[1]/input[1] ").send_keys("菁英汇自动脚本")

#选择省份
shengfen= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[7]/div[1]/select[1] "))
shengfen.select_by_index("2")  # 通过index进行选择,index从0开始
sleep(2)
#选择城市
shengfen= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[7]/div[1]/select[2] "))
shengfen.select_by_index("1")



#报名信息
#使用人姓名
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[1]/div[1]/input[1] ").send_keys("test")
#使用人旺旺
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[2]/div[1]/input[1] ").send_keys("5555555")
#使用人QQ
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[3]/div[1]/input[1] ").send_keys("123456789")
#使用人电话
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[4]/div[1]/input[1] ").send_keys("13355554444")
#老板姓名
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[5]/div[1]/input[1] ").send_keys("老板")
#老板电话
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[6]/div[1]/input[1] ").send_keys("13699998888")


# 店铺基础经营
#店铺层级
cengji= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[1]/div[1]/select[1] "))
cengji.select_by_index("1")
#钻冠级
cengji= Select(driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[1]/div/div/div[6]/div[2]/div/select"))
cengji.select_by_index("1")
#近30天访客数
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[1]/div/div/div[6]/div[3]/div/input").send_keys("136")
#近30天支付额
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[1]/div/div/div[6]/div[4]/div/input").send_keys("13600")
#近30天推广费
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[1]/div/div/div[6]/div[5]/div/input").send_keys("13600")
#货品来源
driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[1]/div[5]/div/div/div[1]/div/div/div[6]/div[6]/div/p/label[1]/input").click()


# 团队结构调研
#店铺团队人数
renshu= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[8]/div[1]/div[1]/select[1] "))
renshu.select_by_index("1")
#团队成员组成
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[2]/div[1]/p[1]/label[1]/input[1] ").click()
#外包
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[3]/div[1]/p[1]/label[1]/input[1] ").click()

# 运营现状能力

#数据分析能力
driver.find_element_by_xpath("//div[@class='store-con']/div[10]/div[1]/div[1]/div[1]/label[1]/input[1] ").click()
#店铺运营能力
driver.find_element_by_xpath("//div[@class='store-con']/div[10]/div[2]/div[1]/div[1]/label[1]/input[1] ").click()
#内容运营能力
driver.find_element_by_xpath("//div[@class='store-con']/div[10]/div[3]/div[1]/div[1]/label[1]/input[1] ").click()
#视觉能力
driver.find_element_by_xpath("//div[@class='store-con']/div[10]/div[4]/div[1]/div[1]/label[1]/input[1] ").click()
#推广能力
driver.find_element_by_xpath("//div[@class='store-con']/div[10]/div[5]/div[1]/div[1]/label[1]/input[1] ").click()
#视觉能力
driver.find_element_by_xpath("//div[@class='store-con']/div[10]/div[6]/div[1]/div[1]/label[1]/input[1]").click()


#点击保存
driver.find_element_by_xpath("//button[@class='submitform margin_l349'] ").click()

driver.quit()