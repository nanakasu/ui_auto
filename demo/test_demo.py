from time import sleep

import pytest
from selenium import webdriver

def test_brower(driver):
    driver.get("http://www.baidu.com")
    sleep(2)
    driver.get("http://www.jd.com")

    #清空

    #清空

