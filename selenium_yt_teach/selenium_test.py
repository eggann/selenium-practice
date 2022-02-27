from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "D:/Python爬蟲練習/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.dcard.tw/f")
search=driver.find_element_by_name("query")
search.send_keys("比特幣")
search.clear()
search.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/h4'))
    )

titles = driver.find_elements_by_class_name("tgn9uw-3")
for title in titles:
    print(title.text)
    
link = driver.find_element_by_partial_link_text("#分享 比特幣走勢")
link.click()
driver.back()
driver.back()
time.sleep(2)
driver.forward()

time.sleep(5)
driver.quit()