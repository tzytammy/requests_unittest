#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: requests_api_test.py
"""
Requests + Unittest接口自动化测试
"""
import requests


def login(url, account, password):
	data = {
		'account': account,
		'password': password
	}
	resp = requests.post(url_1, data=data)
	return resp
	

def test_get_api(url):
	headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
	}
	
	login_url = "http://10.64.83.134/txws_crm/index.php?s=/Pub/public/login"
	account = "晏雪彬"
	passwd = "jiubugaosuni"
	cookies = {
		"PHPSESSID": login(login_url, account, passwd).cookies.get("PHPSESSID")
	}
	resp = requests.get(url, headers=headers, cookies=cookies)
	return resp.text
	

if __name__ == '__main__':
	url = "http://10.64.83.134/txws_crm/index.php?s=/Resource/CustomerFirm/index"
	res = test_get_api(url)
	print(res)
