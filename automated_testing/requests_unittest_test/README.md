# 使用前请阅读以下注意事项 

1、请保证Python版本 > 3.0.0，最好用最新的3.7.0  
2、批量安装所需的第三方依赖库:&nbsp;&nbsp;&nbsp;cd 到requirements.txt所在目录下,执行pip install -r requirements.txt  
3、根目录下run.py为框架入口文件  
4、请修改run.py中第**21**行的目录为自己电脑中存放框架的根目录(这个问题后期会修复，就不用每次都修改目录了)  
5、目前，生成的测试报告有两种类型，可以通过命令行参数传参指定使用哪一种类型:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1-HTMLTestRunner,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2-BeautifulReport  
6、使用BeautifulReport报告，一步即可:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;需要将app/libs/BeautifulReport.zip压缩包解压后放一份到你python的安装目录的Lib下的site-packages下  
7、在PyCharm中，导入框架，在框架根目录上，右键单击，选择Mark Directory as，在出现的二级菜单上,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;选中Sources Root, 将框架根目录设置为源码根目录  

8、关于命令行参数:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a、支持-v/--version，查看框架版本号，第一版暂定为1.0.0。用法：在windows 命令窗口，cd到框架根目录，敲python run.py -v即可，后面的参数用法相同  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b、支持-e/--email，是否发送邮件，传这个可选参数，表示发送，不传，则不发送，默认为不发送  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c、支持-h/--help，查看命令行帮助信息  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d、支持选择生成测试报告的类型，直接传1或2即可，不传的话默认为1。用法：python run.py 1或者python run.py 2，可参考第5条  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e、后期有其他需求，可以再添加其他的命令行参数  
9、关于cookie依赖的问题，目前还有一点小bug，下一个版本争取解决掉  

10、**框架使用**：  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a、写测试用例在app/case目录下，可根据项目情况，自定义用例子目录，用例文件名命名须按照Python  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;官方推荐的命名规范，即驼峰命名法(Python具体的编码风格指南，参考PEP8)，以Test开头  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b、关于框架的目录结构：  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;app目录，主要存放框架的用例(case)、相关依赖库(libs)、工具类库(utils),  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config目录，主要是存放框架配置文件，包括公共配置文件(common.ini)、日志配置(log.ini或者log.json，可自定义日志配置)、邮件配置(mail.ini)，配置文件格式为ini或json，推荐ini格式，可自定义配置文件  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data目录，存放一些依赖数据文件，目前存放了cookie依赖文件(cookie.json)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log目录，存放框架日志，包括公共日志文件(common.log)、错误日志文件(error.log)，可自定义日志文件  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;report目录，存放测试报告  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run.py，框架入口文件  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirements.txt，框架第三方依赖库列表，可用于批量安装这些依赖库  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;README.md，即该文件，使用说明文件  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\_\_init__.py文件，当前包的标识文件，不可删除  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c、框架使用到的Python标准库:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sys  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unittest  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;argparse  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;json  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;smtplib  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;email  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threading  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;configparser  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d、关于Python代码编写，主要遵守两个PEP(Python Enhancement Proposal,Python增强提案)：  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PEP8，即Python风格指南，也是整个Python社区都共同遵守的编码规范；  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PEP20，即Python之禅(The Zen of Python)，这份提案给我们展示了Python的设计哲学，可以为我们编码提供指导  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e、配置问题  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;发送邮件需要配置自己的邮件服务器、发件人、收件人、发件人邮箱密码，具体配置可参考config/mail.ini；  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;日志配置问题，使用的是标准库中的logging模块，具体配置和用法，大家可Google，日志配置有三种方式：配置文件中配置、字典配置、代码配置  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其他一些公共配置项，可以放在common.ini中

11、下一个大版本解决的问题：  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a、cookie依赖小bug  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b、mock模拟  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c、测试pytest框架  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d、测试新的报告框架Allure  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e、重写一些目前觉得比较low的代码  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f、命令行功能，准备参考howdoi，做一个可执行文件  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g、修改目录相关的问题
