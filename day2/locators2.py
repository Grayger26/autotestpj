import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

time.sleep(2)

#CSS Selectors:
# ----------
# tag + id
# tag + class
# tag + attribute
# tag + class + attribute

# tag + id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# tag + class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc")

# tag + attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc")

# tag + class + attribute
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("password")

time.sleep(2)

driver.find_element(By.CLASS_NAME, "_9lsa").click()

time.sleep(2)

driver.quit()