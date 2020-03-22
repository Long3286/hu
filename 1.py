from selenium import webdriver
from time import sleep
# 实现规避检测模块
from selenium.webdriver import ChromeOptions
# 无头浏览器模块
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 无头浏览器浏览
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 获取用户名和密码
name = input('请输入用户名')
password = input('请输入密码')
print('请耐心等待15秒......')
print('运行完毕之后请打开目录下的1.png文件查看提交成功截图')
# 创建浏览器对象
browser = webdriver.Chrome(chrome_options=chrome_options,options=option)
browser.get('http://jkxxcj.zjhu.edu.cn/login.html')
sleep(3)
zh_input = browser.find_element_by_id('zgh').send_keys(name)
mm_input = browser.find_element_by_id('mm').send_keys(password)
sleep(2)
login_button = browser.find_element_by_id('loginBtn')
login_button.click()
sleep(4)
# 提交健康情况
health = browser.find_element_by_id('jkbg')
health.click()
sleep(3)
send = browser.find_element_by_id('saveBtn')
send.click()
sleep(4)
# 截屏，验证是否成功
browser.save_screenshot('1.png')
browser.quit()