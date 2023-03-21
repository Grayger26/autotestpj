import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

link = "http://suninjuly.github.io/find_xpath_form "

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "first_name")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
button.click()


time.sleep(30)

browser.quit()
