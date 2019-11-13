from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(1)

    input = driver.find_element_by_xpath("//input[@name='t1']")

    input.clear

    input.send_keys("1212")
    sleep(1)


def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(3)

    radio = driver.find_element_by_xpath("//input[@value=1]")
    radio.click()
    sleep(1)

def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(3)

    select = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    select.click()
    sleep(2)
    option = driver.find_elements_by_xpath("(//span[text()='双皮奶'])[last()]")
    sleep(3)
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)

def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)
    slider = driver.find_elements_by_xpath("//*[@id='form']/form/div[5]/div/div/div/div[2]/div")
    slider.click()
    sleep(2)



def test_input(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(1)

    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[1]/div/div/input")

    t1.clear()

    t1.send_keys("14:15:11")
    sleep(2)


def test_upload(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(1)

    file = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")

    file.clear()
    file.send_keys("C:\\Users\\guoya\\Desktop\\_20191113144411.jpg")
    sleep(2)

