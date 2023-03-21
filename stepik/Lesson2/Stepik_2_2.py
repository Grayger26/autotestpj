import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://suninjuly.github.io/get_attribute.html")
driver.maximize_window()

time.sleep(2)

x_element = driver.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

driver.find_element(By.ID, "answer").send_keys(y)
driver.find_element(By.ID, "robotCheckbox").click()
driver.find_element(By.ID, "robotsRule").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(20)

driver.quit()

