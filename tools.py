from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def ele_click(driver, xpath, text1:str='',timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        print(text1+"按钮点击完毕")
    except TimeoutException:
        print(text1+"按钮等待超时")

def ele_send_keys(driver, xpath, text, text1:str='',timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.clear()
        element.send_keys(text)
        print(text1+"输入框输入完毕")
    except TimeoutException:
        print(text1+"输入框等待超时")

def ele_get_text(driver, xpath, text1:str="",timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        text = element.text
        print(f"获取{text1}成功: {text}")
        return text
    except TimeoutException:
        print("等待元素超时")
        return None

def ele_is_displayed(driver, xpath, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        is_visible = element.is_displayed()
        print(f"元素可见: {is_visible}")
        return is_visible
    except TimeoutException:
        print("等待元素超时")
        return False

def ele_wait_until_disappear(driver, xpath, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.XPATH, xpath))
        )
        print("元素已消失")
        return True
    except TimeoutException:
        print("元素未消失")
        return False

