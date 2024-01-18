import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
url = "https://estudijas.rtu.lv/my/"
driver.get(url)
time.sleep(2)
find = driver.find_element(By.ID, "submit")
find.click()
time.sleep(3)