import selenium
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
res = ""
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
saturs = driver.page_source
esaturs = bs4.BeautifulSoup(saturs, 'html.parser')
atrada = esaturs.find('section', id='inst1602648', class_='block_calendar_upcoming block card mb-3') 
atrada1 = atrada.find_all('div', class_="overflow-auto")
if atrada1 != None:
    for element in atrada1:
        for child in element:
            if "Rīt" in str(child):
                print ("LAIKS DARĪT")
                res = res + "1"
                temp = element.find('a', class_="text-truncate")
                temp = str(temp)
                pos1 = temp.find("href")
                pos2 = temp.find("</a>")
                temp = temp[pos1+5:pos2]
                print (temp)
res = res + "."
if res == ".":
    print ("varu tālāk nokrastinēt!")