import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get("http://suninjuly.github.io/explicit_wait2.html")

button = driver.find_element(By.ID, "book")

text100 = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button.click()

driver.execute_script("window.scrollBy(0, 150);")

x = driver.find_element(By.ID, "input_value").text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

driver.find_element(By.ID, "answer").send_keys(y)

driver.find_element(By.ID, "solve").click()

alert = driver.switch_to.alert.text

print(alert)

driver.quit()