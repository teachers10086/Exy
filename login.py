from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tools import ele_click, ele_send_keys
# import configparser

username = input("请输入账号：")
password = input("请输入密码：")


def login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    login_url = "https://avaryholding.yunxuetang.cn/login.html"
    driver.get(login_url)

    ele_send_keys(driver, "(//input[@name='username'])[1]", username, text1="账号")
    ele_send_keys(driver, "(//input[@name='username'])[2]", password, text1="密码")
    ele_click(driver, "(//input[@id='secretProtocol'])[2]", text1="协议")
    ele_click(driver, "(//span[@class='standard-size-16'])[2]", text1="登录")

    return driver
