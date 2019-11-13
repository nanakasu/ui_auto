from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome('../chromedrive78/chromedriver.exe')
    sleep(1)
    #调整窗口大小
    driver.maximize_window()
    sleep(3)
    yield driver

    driver.quit()