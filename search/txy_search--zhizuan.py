#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import common.CsvDataRead as cdr

FILE_PATH = "data.csv"

if __name__ == '__main__':
    dataRead = cdr.CsvDataRead(FILE_PATH)
    url = dataRead.get_url_from_data_file(6)

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

#报名人信息
#报名人姓名
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[1]/div[1]/input[1] ").send_keys("特训营")
#报名人联系方式
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[2]/div[1]/input[1] ").send_keys("13655554478")
#报名人职位
zhiwei= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[3]/div[1]/select[1] "))
zhiwei.select_by_index("1")
#报名人年龄段
age= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[2]/div[4]/div[1]/select[1] "))
age.select_by_index("1")

# 填写店铺基本信息
#店铺类目
leimu= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[2]/div[1]/select[1] "))
leimu.select_by_index("1")
#店铺链接
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[3]/div[1]/input[1] ").send_keys("http://www.taobao.com")
#所在省份
shengfen= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[4]/div[1]/select[1] "))
shengfen.select_by_index("2")
sleep(3)
#所在城市
chengshi= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[4]/div[1]/select[2] "))
chengshi.select_by_index("2")
#店铺层级
cengji= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[5]/div[1]/select[1] "))
cengji.select_by_index("1")
#近1年销售额
money= Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[6]/div[1]/select[1] "))
money.select_by_index("1")
#开店时长
longtime=Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[7]/div[1]/select[1] "))
longtime.select_by_index("2")
#电商团队人数
peoplenum=Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[4]/div[8]/div[1]/select[1] "))
peoplenum.select_by_index("2")

# 团队构成
driver.find_element_by_xpath("//div[@class='store-con']/div[4]/div[9]/div[1]/p[1]/label[1]/input[1]").click()
#其他电商渠道
driver.find_element_by_xpath("//div[@class='store-con']/div[4]/div[10]/div[1]/p[1]/label[1]/input[1]").click()
#供应链情况
driver.find_element_by_xpath("//div[@class='store-con']/div[4]/div[11]/div[1]/p[1]/label[1]/input[1]").click()
#店铺类型
driver.find_element_by_xpath("//div[@class='store-con']/div[4]/div[12]/div[1]/p[1]/label[1]/input[1]").click()
#近30天直通车花费金额
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[13]/div[1]/input[1] ").send_keys("1122")
#近30天直通车R0I
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[14]/div[1]/input[1] ").send_keys("11220")
#近30天钻展花费金额
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[15]/div[1]/input[1] ").send_keys("11221")
#近30天钻展ROI
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[16]/div[1]/input[1] ").send_keys("11223")

#产品平均毛利率
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[18]/div[1]/input[1] ").send_keys("112")
#对于直通车最想了解的知识点
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[19]/div[2]/p[1]/label[1]/input[1] ").click()
#对于钻展最想了解的知识点
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[20]/div[1]/p[1]/label[1]/input[1] ").click()
#除了这个主题还有哪些是您目前急需了解的
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[21]/div[1]/p[1]/label[1]/input[1]").click()
#描述一下您的直通车推广现状
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[22]/div[2]/textarea[1]").send_keys("直通车现状")
#描述一下您的钻展推广现状
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[4]/div[23]/div[2]/textarea[1]").send_keys("钻展现状")

#点击下一步

driver.find_element_by_xpath("//button[@class='submitform margin_l140'] ").click()

# 第二页报名学员信息
#参加人姓名
driver.find_element_by_xpath("//div[ @class ='store-con']/div[5]/div[2]/div[1]/div[1]/input[1]").send_keys("钻展现状")

#参加人联系方式
driver.find_element_by_xpath("//div[ @class ='store-con']/div[5]/div[2]/div[2]/div[1]/input[1]").send_keys("13655554777")
#参加人职位
zhiwei=Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[5]/div[2]/div[3]/div[1]/select[1]"))
zhiwei.select_by_index("1")
#参加人年龄段
age=Select(driver.find_element_by_xpath("//div[ @class ='store-con']/div[5]/div[2]/div[4]/div[1]/select[1]"))
age.select_by_index("1")

#点击保存
driver.find_element_by_xpath("//button[@class='submitform margin_l20'] ").click()
sleep(3)
driver.quit()
