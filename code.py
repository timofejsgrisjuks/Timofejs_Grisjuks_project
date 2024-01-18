import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print ("password!")
password = input()
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
url = "https://estudijas.rtu.lv/my/"
driver.get(url)
time.sleep(2)
find = driver.find_element(By.ID, "submit")
find.click()
time.sleep(2)
find = driver.find_element(By.ID, "IDToken1")
find.send_keys("timofejs.grisjuks")
time.sleep(1)
find = driver.find_element(By.ID, "IDToken2")
find.send_keys(password)
time.sleep(1)
webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
time.sleep(2)