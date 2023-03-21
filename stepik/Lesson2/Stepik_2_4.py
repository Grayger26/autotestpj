import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://suninjuly.github.io/redirect_accept.html")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "button.trollface").click()

new_window = driver.window_handles[1]

driver.switch_to.window(new_window)

x = driver.find_element(By.ID, "input_value").text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

driver.find_element(By.ID, "answer").send_keys(y)

driver.find_element(By.CSS_SELECTOR, "button.btn[type=submit]").click()

time.sleep(1)

alert_text = driver.switch_to.alert.text

print(alert_text)

driver.quit()

# При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера.
# WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:
# browser.switch_to.window(window_name)

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
# new_window = browser.window_handles[1]

# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]
# После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.