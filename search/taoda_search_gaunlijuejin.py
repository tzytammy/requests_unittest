#coding=utf-8
#淘大-管理掘金

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import  sleep
import common.CsvDataRead as cdr

FILE_PATH = "data.csv"

if __name__ == '__main__':
    dataRead = cdr.CsvDataRead(FILE_PATH)
    url = dataRead.get_url_from_data_file(3)

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

#基本信息
#主营店铺所属类目
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[3]/div[1]/select[1] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#店铺链接
driver.find_element_by_xpath("//div[ @class ='store-con'] /div[2]/div[4]/div[1]/input[1] ").send_keys("http://www.taobao.com")
# 实例化一个Select类的对象
#主营店铺所在省市
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[5]/div[1]/select[1] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[5]/div[1]/select[2] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#主营店铺开店时长
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[6]/div[1]/select[1] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#主营店铺类型
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[7]/div[1]/select[1]  "))
zhuyingdianpusuoshuleimu.select_by_index("1")  # 通过index进行选择,index从0开始
#各平台其他店铺
driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[8]/div[1]/p[1]/label[1]/input[1] ").click()
driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[8]/div[1]/p[1]/label[1]/input[2] ").send_keys("1")
#供货渠道及产品是否多样化
driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[9]/div[1]/p[1]/label[1]/input[1] ").click()
# 店铺层级
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[10]/div[1]/select[1] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#店铺整体转化率
driver.find_element_by_xpath("//div[@class='store-con']/div[2]/div[11]/div[1]/input[1] ").send_keys("20")


#团队信息
#电商团队的人数
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/select[1] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#店铺外包
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/p[1]/label[1]/input[1] ").click()


#店铺经营数据
#店铺每月投入的营销费用
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/select[1] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#过去12个月的店铺交易额
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/select[1]  "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始


#学习需求
#您的团队需要哪些方面的知识学习： [请在方框内依次排序写入字母]
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[3]/span[1]/input[1]  ").send_keys("A")
#请您结合团队管理情况说说管理中的困惑？
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[4]/div[1]/textarea[1]  ").send_keys("A")
#您期望从本次课程中学到哪些东西？
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[5]/div[1]/textarea[1]  ").send_keys("A")


#点击下一步
driver.find_element_by_xpath("//button[@class='submitform margin_l140 ng-scope'] ").click()





#学员信息
#学员姓名
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/input[1] ").send_keys("cxt")
#学员职务
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/input[1] ").send_keys("cxt")
#学员联系方式
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/div[3]/div[1]/input[1] ").send_keys("18000000000")
#学员常用邮箱
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/div[4]/div[1]/input[1]  ").send_keys("123@qq.com")
#学员出生年份
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/div[5]/div[1]/select[1] "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始
#学员从事电商的时间
zhuyingdianpusuoshuleimu= Select(driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/div[6]/div[1]/select[1]  "))
zhuyingdianpusuoshuleimu.select_by_index("3")  # 通过index进行选择,index从0开始


#点击保存
driver.find_element_by_xpath("//button[@class='submitform ng-scope margin_l20'] ").click()

#driver.quit()

