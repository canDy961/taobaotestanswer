# api 接口测试
##  准备工作
1、安装依赖包
# requests  用户发起http请求
# 

2.运行测试用例
# 登录接口 
url= https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0&_bx-v=2.0.31
请求方式：post
校验内容：
校验请求返回状态 
校验请求参数cookie

# 搜索接口
url=https://s.taobao.com/search?q=111&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210614&ie=utf8
请求方式：get
校验请求返回状态
校验请求参数cookie

