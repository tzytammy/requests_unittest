#coding=utf-8
#菁英汇-研修班
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import common.CsvDataRead as cdr

FILE_PATH = "data.csv"

if __name__ == '__main__':
    dataRead = cdr.CsvDataRead(FILE_PATH)
    url = dataRead.get_url_from_data_file(2)

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

#店铺基本信息
#经营年限
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[3]/div[1]/input[1]").send_keys("2")
#店铺链接
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[4]/div[1]/input[1]").send_keys("http://www.taobao.com")
#选择类目
# 实例化一个Select类的对象
leimu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[5]/div[1]/select[1] "))
# 下面三种方法用于选择"篮球运动员"
leimu.select_by_index("2")  # 通过index进行选择,index从0开始
#店铺名称
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[6]/div[1]/input[1] ").send_keys("cxt")
#选择省份
shengfen= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[7]/div[1]/select[1] "))
shengfen.select_by_index("2")  # 通过index进行选择,index从0开始
#选择城市
shengfen= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[7]/div[1]/select[2] "))
shengfen.select_by_index("1")


# 店铺基础经营
#店铺层级
dianpucengji= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[1]/div[1]/select[1] "))
dianpucengji.select_by_index("2")
sleep(3)
#近30天访客数
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[2]/div[1]/input[1] ").send_keys("100")
#近30天支付额
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[3]/div[1]/input[1] ").send_keys("100")
#近30天推广费
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[4]/div[1]/input[1] ").send_keys("100")
#货品来源
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[5]/div[1]/p[1]/label[1]/input[1] ").click()


# 团队结构调研
#店铺团队人数
renshu= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[1]/div[1]/select[1] "))
renshu.select_by_index("1")
#专职运营人数
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[2]/div[1]/select[1] "))
renshu.select_by_index("1")
#专职推广人数
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[3]/div[1]/select[1] "))
renshu.select_by_index("1")
#专职美工人数
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[4]/div[1]/select[1] "))
renshu.select_by_index("1")
#专职客服人数
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[5]/div[1]/select[1] "))
renshu.select_by_index("1")
#专职品牌策划人数
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[6]/div[1]/select[1] "))
renshu.select_by_index("1")
#专职运法务人数
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[7]/div[1]/select[1] "))
renshu.select_by_index("1")
#专职财务人数
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[8]/div[1]/select[1] "))
renshu.select_by_index("1")
#团队划分
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[9]/div[1]/select[1] "))
renshu.select_by_index("1")
#现有团队中是否有店长、运营主管、推广主管等中层梯队？
renshu = Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[6]/div[10]/div[1]/select[1] "))
renshu.select_by_index("1")

# 运营现状能力

#数据分析能力
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[1]/div[1]/div[1]/label[1]/input[1] ").click()
#店铺运营能力
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[2]/div[1]/div[1]/label[1]/input[1] ").click()
#内容运营能力
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[3]/div[1]/div[1]/label[1]/input[1] ").click()
#视觉能力
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[4]/div[1]/div[1]/label[1]/input[1]").click()
#推广能力
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[5]/div[1]/div[1]/label[1]/input[1]").click()
#视觉能力
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[8]/div[6]/div[1]/div[1]/label[1]/input[1] ").click()


#点击保存
driver.find_element_by_xpath("//button[@class='submitform margin_l349'] ").click()
sleep(3)
#driver.quit()
