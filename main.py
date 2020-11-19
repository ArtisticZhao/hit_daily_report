# coding: utf-8
import time
from selenium import webdriver


USERNAME = "YOUR_USERNAME"
PASSWD = "YOUR_PASSWORD"

if __name__ == "__main__":
    URL = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsHome"
    driver = webdriver.Chrome()
    driver.get(URL)
    username_input = driver.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(USERNAME)
    passwd_input = driver.find_element_by_id("password")
    passwd_input.clear()
    passwd_input.send_keys(PASSWD)
    button_login = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()
    time.sleep(1)
    driver.find_element_by_id("mrsb").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a/div").click()
    time.sleep(1)
    # here will pop up a alert window
    al = driver.switch_to_alert()
    al.accept()
    modify = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]")
    modify.click()
    time.sleep(1)
    # check the checkbox
    driver.find_element_by_id("txfscheckbox").click()
    # submit
    driver.find_element_by_xpath("/html/body/div[5]").click()
