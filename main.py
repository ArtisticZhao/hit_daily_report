# coding: utf-8
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import sys


get_pre_location_js = '''$.ajax({
    url : "/zhxy-xgzs/xg_mobile/xsMrsb/getYqxx",
    type : "Post",
    dataType : "json",
    data : {info:JSON.stringify({id : id})},
    success : function(result) {
        var data = result.module.data[0];
        $("#gnxxdz").val(data.gnxxdz);
    }
});
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
    driver = webdriver.Firefox()
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

    # daily report
    URL = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/yqxx"
    # allow position
    profile = webdriver.FirefoxProfile()
    profile.set_preference("geo.prompt.testing", True)
    profile.set_preference("geo.prompt.testing.allow", False)

    # open report page
    driver = webdriver.Firefox(firefox_profile=profile)
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
    #  # open daily report
    #  driver.find_element_by_id("mrsb").click()
    # click add button
    driver.execute_script("javascript:add();")
    #  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a/div").click()
    time.sleep(1)
    # deal with Alert
    result = EC.alert_is_present()(driver)
    if result:
        print(result.text)
        result.accept()
        # click modify herf
        modify = driver.find_element_by_xpath('//div[contains(@onclick, "\'0\'")]')
        #  print(modify)
        #  sys.exit(0)
        #  modify = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]")
        modify.click()
        time.sleep(5)
    else:
        print("alert 未弹出！")
    # deal with Alert: here the web will try to get your locations
    # but if the browse block will popup a alert
    time.sleep(5)
    result = EC.alert_is_present()(driver)
    if result:
        print(result.text)
        result.accept()
    else:
        print("alert 未弹出！")

    # process the location!!!
    driver.execute_script(get_pre_location_js)
    time.sleep(1)

    # check the checkbox
    driver.find_element_by_id("checkbox").click()
    # submit
    driver.find_element_by_class_name('right_btn').click()

    driver.find_element_by_xpath('//a[contains(text(), "确定")]').click()
    time.sleep(5)
    # save the result
    driver.save_screenshot(sys.argv[1]+".png")
    print(sys.argv[1] + " : OK")
    driver.close()
