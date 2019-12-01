from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


def get_driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:62001",
        "appPackage": "com.tencent.mm",
        "noReset": "True",
        "appActivity": ".plugin.sns.ui.SnsTimeLineUI"
    }
    # .plugin.sns.ui.SnsTimeLineUI   .plugin.sns.ui.SnsTimeLineUI
    # desired_caps['platformName'] = "Android"  # 声明是ios还是Android系统
    # desired_caps['platformVersion'] = '5.1.1'  # Android内核版本号，可以在夜神模拟器设置中查看
    # desired_caps['deviceName'] = '127.0.0.1:62001'  # 连接的设备名称
    # desired_caps['appPackage'] = 'com.tencent.mm'
    # desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


def to_pyq():
    driver = get_driver()
    driver.implicitly_wait(10)
    # driver.find_element_by_id('com.tencent.mm:id/cw3').click()
    # driver.find_element_by_link_text('朋友圈').click()
    # ele = driver.find_element_by_id("com.tencent.mm:id/j1")
    driver.tap(positions=[(1015, 100)], duration=2000)
    # actions = ActionChains(driver)
    # actions.click_and_hold(ele)
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    time.sleep(3)
    driver.find_element_by_xpath(
        '//android.widget.FrameLayout[@content-desc="当前所在页面,发表文字"]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText').send_keys(
        '这是一条来自python自动化测试的朋友圈' + '\n' + now_time)
    driver.find_element_by_id('com.tencent.mm:id/j0').click()


if __name__ == '__main__':
    to_pyq()
