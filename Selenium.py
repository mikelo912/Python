# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:16:05 2023

@author: s9571
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument('--user-agent=%s' % user_agent)

service = Service(executable_path='./chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#將webdriver設定為undefined
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get : () -> undefined
        })
    """
    })

driver.get('https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates')