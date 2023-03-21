import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://suninjuly.github.io/alert_accept.html")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "button.btn[type=submit]").click()

alert = driver.switch_to.alert
alert.accept()

x = driver.find_element(By.ID, "input_value").text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

driver.find_element(By.ID, "answer").send_keys(y)

driver.find_element(By.CSS_SELECTOR, "button.btn[type=submit]").click()

time.sleep(5)

alert2 = driver.switch_to.alert
alert_text = alert2.text

print(alert_text)

driver.quit()





# Теперь рассмотрим ситуацию, когда в сценарии теста возникает необходимость не только получить содержимое alert,
# но и нажать кнопку OK, чтобы закрыть alert. Alert является модальным окном: это означает, что пользователь
# не может взаимодействовать дальше с интерфейсом, пока не закроет alert. Для этого нужно сначала переключиться на окно с alert,
# а затем принять его с помощью команды accept():
# alert = browser.switch_to.alert
# alert.accept()

# Чтобы получить текст из alert, используйте свойство text объекта alert:
# alert = browser.switch_to.alert
# alert_text = alert.text

# Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm.
# Для переключения на окно confirm используется та же команда, что и в случае с alert:
# confirm = browser.switch_to.alert
# confirm.accept()

# Для confirm-окон можно использовать следующий метод для отказа:
# confirm.dismiss()
# То же самое, что и при нажатии пользователем кнопки "Отмена".
#
# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()