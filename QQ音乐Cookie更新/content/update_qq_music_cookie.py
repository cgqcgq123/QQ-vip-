import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import re
import sys
from selenium.webdriver.chrome.service import Service
import os

sys.path.append('.\\')

if __name__ == '__main__':
    chrome_driver_path = '.\chromedriver.exe'
    service = Service(executable_path=chrome_driver_path)
    chrome = webdriver.Chrome(service=service)
    print("程序正在启动...")
    chrome.get('https://y.qq.com/')
    chrome.maximize_window()
    chrome.implicitly_wait(1000)
    while True:
        element = chrome.find_element(By.CLASS_NAME, 'top_login__link')
        time.sleep(1.5)
        try:
            txt = element.text
            if txt != "登录":
                break
            print("请登录绿钻账号！！")
        except:
            break
    os.system('cls')
    chrome.execute_script('alert(document.cookie)')
    switch = chrome.switch_to.alert
    alert = switch.text
    switch.accept()
    chrome.close()
    qm_keyst = re.search(r'qm_keyst=.*?;', alert).group()[9:-1]
    uin = re.search(r';\suin=.*?;', alert).group()[6:-1]
    # print(qm_keyst)
    # print(uin)
    cookie = f'{qm_keyst}&{uin}'
    # print(cookie)
    with open('.\cookies\qm_cookie', 'w', encoding='utf-8') as f:
        f.write(cookie)
    f.close()
    input("运行完毕,按任意键退出!!")
