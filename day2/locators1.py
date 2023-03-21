import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

time.sleep(2)

# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.CLASS_NAME, "search-box-button").click()

# driver.find_element(By.LINK_TEXT, "Register").click()

# slider = driver.find_elements(By.CLASS_NAME, "nivo-imageLink")
# print("Number of sliders: ", len(slider))
#
# links = driver.find_elements(By.TAG_NAME, "a")
# print("Number of links: ", len(links))

time.sleep(3)

driver.quit()