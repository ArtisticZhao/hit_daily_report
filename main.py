# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python main.py id passwd")
        sys.exit(-1)
    URL = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsHome"
    driver = webdriver.Chrome()
    driver.get(URL)
    # login
    username_input = driver.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(sys.argv[1])
    passwd_input = driver.find_element_by_id("password")
    passwd_input.clear()
    passwd_input.send_keys(sys.argv[2])
    button_login = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()
    time.sleep(1)
    # open daily report
    driver.find_element_by_id("mrsb").click()
    # click add button
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a/div").click()
    time.sleep(1)
    # deal with Alert
    result = EC.alert_is_present()(driver)
    if result:
        print(result.text)
        result.accept()
    else:
        print("alert 未弹出！")
    # click modify herf
    modify = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]")
    modify.click()
    time.sleep(1)
    # deal with Alert: here the web will try to get your locations
    # but if the browse block will popup a alert
    result = EC.alert_is_present()(driver)
    if result:
        print(result.text)
        result.accept()
    else:
        print("alert 未弹出！")
    # check the checkbox
    driver.find_element_by_id("txfscheckbox").click()
    # submit
    driver.find_element_by_xpath("/html/body/div[5]").click()
    # save the result
    driver.save_screenshot(sys.argv[1]+".png")

    driver.quit()
