# coding: utf-8
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import sys
import random

DRIVER = "Chrome"
RANDOM_HOUR = 1

get_pre_location_js = '''$.ajax({
    url : "/zhxy-xgzs/xg_mobile/xsMrsb/getYqxx",
    type : "Post",
    dataType : "json",
    data : {info:JSON.stringify({id : id})},
    success : function(result) {
        var data = result.module.data[0];
        $("#gnxxdz").text(data.gnxxdz);
    }
});
'''
set_location_js = '''
$("#gnxxdz").text("黑龙江省哈尔滨市香坊区王兆街道航天路哈尔滨工业大学科学园(文政街)");
'''
get_out_data_js = '''
    // 获取当前日期
    var date = new Date();

    var tomorrow = new Date();
    tomorrow.setDate(new Date().getDate()+1);
    date = tomorrow;

    // 获取当前月份
    var nowMonth = date.getMonth() + 1;
    // 获取当前是几号
    var strDate = date.getDate();
    // 添加分隔符“-”
    var seperator = "-";
    // 对月份进行处理，1-9月在前面添加一个“0”
    if (nowMonth >= 1 && nowMonth <= 9) {
       nowMonth = "0" + nowMonth;
    }
    // 对日期进行处理，1-9号在前面添加一个“0”
    if (strDate >= 0 && strDate <= 9) {
       strDate = "0" + strDate;
    }
    // 最后拼接字符串，得到一个格式为(yyyy-MM-dd)的日期
    var rq = date.getFullYear() + seperator + nowMonth + seperator + strDate;
    var data = {
                rq  : rq,
                cxly  : "吃饭",
                cxlx  : "01",
                yjlxjsrq  : "",
                id : id,
                yqlxlx : "",
                yqlxsy : "",
                lsjcjg : "",
                lsbgcjyy : "",
                lsjcsj : "",
                lsljjkmys : "",
                lsdsjxcmys : ""
        }
    $.ajax({
            async: false,
            url : "/zhxy-xgzs/xg_mobile/xsCxsq/saveCxsq",
            type : "POST",
            dataType : "json",
            data : {info:JSON.stringify({model : data})},
            success: function(result){
                if(result.isSuccess){
                    $.alert("提交成功");
                }else{
                    $.toptip(result.msg);
                }
            },
            error : function(){
                $.toptip("操作失败");
            }
        });
'''


def go_outside():
    URL = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/yqxx"
    URL_OUT = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsCxsq"
    # open report page
    if DRIVER == "Firefox":
        driver = webdriver.Firefox()
    elif DRIVER == "Chrome":
        driver = webdriver.Chrome()
    driver.get(URL)
    # login
    username_input = driver.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(sys.argv[1])
    passwd_input = driver.find_element_by_id("password")
    passwd_input.clear()
    passwd_input.send_keys(sys.argv[2])
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()
    time.sleep(1)
    driver.get(URL_OUT)

    # click add button
    driver.execute_script("javascript:add();")
    time.sleep(5)
    # request
    driver.execute_script(get_out_data_js)
    time.sleep(5)
    driver.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("""Usage:
                    [daily report] python main.py id passwd
                    [go outside]   python main.py id passwd outside""")
        sys.exit(-1)
    if (len(sys.argv) == 4):
        if sys.argv[3] == "outside":
            go_outside()
            sys.exit(0)

    delay_time_random = 0  # random.randint(0, RANDOM_HOUR*3600)
    print("deley " + str(delay_time_random) + "s")
    time.sleep(delay_time_random)

    print(sys.argv[1])
    # daily report
    URL = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew"
    # allow position
    profile = webdriver.FirefoxProfile()
    profile.set_preference("geo.prompt.testing", True)
    profile.set_preference("geo.prompt.testing.allow", False)

    # --------- open report page
    if DRIVER == "Firefox":
        driver = webdriver.Firefox(firefox_profile=profile)
    elif DRIVER == "Chrome":
        driver = webdriver.Chrome()
    driver.get(URL)
    # --------- login
    username_input = driver.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(sys.argv[1])
    passwd_input = driver.find_element_by_id("password")
    passwd_input.clear()
    passwd_input.send_keys(sys.argv[2])
    button_login = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()
    time.sleep(1)

    # --------- open daily report
    # get location
    driver.execute_script("map();")
    #  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a/div").click()
    time.sleep(1)
    # show location
    loc = driver.execute_script("return $('#dtjwd')[0].innerText")
    print(loc)
    if(loc.find("哈尔滨") < 0):
        print("检测不在哈尔滨，自己上报吧")
        driver.close()
        sys.exit()

    # --------- check the checkbox
    driver.execute_script("$('#txfscheckbox')[0].checked = true")

    #  # scroll to bottom
    #  driver.execute_script("document.documentElement.scrollTop=100000")

    # --------- submit
    driver.execute_script("save();")
    time.sleep(0.5)

    # --------- save the result
    driver.save_screenshot(sys.argv[1]+".png")
    print(sys.argv[1] + " : OK")
    print()
    driver.close()
