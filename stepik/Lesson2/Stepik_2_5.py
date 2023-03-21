from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get("http://suninjuly.github.io/wait1.html")

button = driver.find_element(By.ID, "verify")
button.click()
message = driver.find_element(By.ID, "verify_message")

assert "successful" in message.text