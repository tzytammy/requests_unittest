'''
尽管Requests库功能很友好、开发简单（其实除了import外只需一行主要代码），但其性能与专业爬虫相比还是有一定差距的。
请编写一个小程序，“任意”找个url，测试一下成功爬取100次网页的时间。（某些网站对于连续爬取页面将采取屏蔽IP的策略，所以，要避开这类网站。）
'''
import requests
import time

def HTMLGET(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

sum=0
start=time.perf_counter()
url = "http://www.atstudy.com/"
for i in range(100):
    time1=time.perf_counter()
    HTMLGET(url)
    time2=time.perf_counter()
    every=time2-time1
    sum=sum+every
    print("第{:2d}需要时间为{:.2f}s".format(i+1,every))
end=time.perf_counter()
print ("100次访问总时间为",sum)
print("100次访问总时间为",end-start)


