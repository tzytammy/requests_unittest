'''
程序的结构设计
步骤1：提交商品搜索请求，循环获取页面
步骤2：对于每个页面，提取商品名称和价格信息
步骤3：将信息输出到屏幕上
'''
import re
import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print()
        return r.text
    except:
            return ''

def parsePage(list,html):
    try:
        price=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        name=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range (len(price)):
            reallprice=eval(price[i].split(':')[1])
            reallname=eval(name[i].split(':')[1])
            list.append([reallprice,reallname])
    except:
        print("")

def printGoodsList(list):
    mould="{:4}\t{:8}\t{:16}"
    print(mould.format("序号","价格","商品名称"))
    count=0
    for g in list:
        count=count+1
        print(mould.format(count,g[0],g[1]))

def main():
    goods='书包'
    depth=3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
main()