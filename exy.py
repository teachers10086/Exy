from tools import ele_click, ele_get_text,ele_is_displayed
from login import login

driver = login()

ele_click(driver, "(//span[@class='ellipsis'])[5]", text1="查看全部")
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])
ele_click(driver,"(//input[@class='yxtf-input__inner yxtf-input__inner--border'])[1]",text1="选择课程类型")
ele_click(driver,"(//li[@class='yxtf-select-dropdown__item'])[3]",text1="选择视频课程")

def main():
    try:
        x = 1
        while x < 46:
            for i in range(1,17):
                ele_click(driver,f"(//div[@class='kng-list-new__cover'])[{i}]",text1=f"已点击第{i}个课程")
                a = ele_get_text(driver,"//span[@class='opacity8 ml8']",text1="完成进度")
                if a == "已完成学习":
                    ele_click(driver, "//div[@class='yxtulcdsdk-flex-center yxtulcdsdk-play-goback mr12 hand']",text1="退出课程")
                    ele_is_displayed(driver, "(//input[@class='yxtf-input__inner yxtf-input__inner--border'])[1]")
                    continue
                ele_click(driver,"//span[contains(@class, 'yxtulcdsdk-flex-center-center')]/ancestor::button",text1="开始学习")
                b = ele_get_text(driver,"//span[text()='已完成学习']",text1="完成进度",timeout=12000)
                if b:
                    ele_click(driver, "//div[@class='yxtulcdsdk-flex-center yxtulcdsdk-play-goback mr12 hand']",text1="退出课程")
                    ele_is_displayed(driver, "(//input[@class='yxtf-input__inner yxtf-input__inner--border'])[1]")
                    continue
            ele_click(driver,"//button[@class='btn-next transformrtl']",text1="下一页")
            x += 1
    except :
        print("程序错误，已退出！")

if __name__ == "__main__":
    main()
