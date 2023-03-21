import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get("https://www.onliner.by/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input.fast-search__input").send_keys("Iphone")

driver.find_element(By.CSS_SELECTOR, "ul")

time.sleep(10)

driver.quit()