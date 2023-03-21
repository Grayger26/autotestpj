from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get("http://suninjuly.github.io/wait2.html")

button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

button.click()

message = driver.find_element(By.ID, "verify_message")

assert "successful" in message.text


driver.quit()


# В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:
#
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present

# Описание каждого правила можно найти на https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions.