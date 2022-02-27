from ast import keyword
from re import search
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import wget

PATH = "D:/Python爬蟲練習/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = 'https://www.instagram.com/'
driver.get(url)
           
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.NAME, 'username'))
)


username_input = driver.find_elements_by_name('username')[0]
password_input = driver.find_elements_by_name('password')[0]
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')

username_input.clear()
password_input.clear()
username_input.send_keys('annyaegg102')
password_input.send_keys('')
login.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input'))
)
search_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input')
search_input.clear()
keyword = '#dog'
search_input.send_keys(keyword)
time.sleep(1)
search_input.send_keys(Keys.RETURN)
time.sleep(1)
search_input.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'FFVAD'))
)
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

imgs = driver.find_elements_by_class_name('FFVAD')

path = os.path.join(keyword)
os.mkdir(path)

count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    print(img.get_attribute('src'))
    wget.download(img.get_attribute('src'), save_as)
    # time.sleep(1)
    count += 1
