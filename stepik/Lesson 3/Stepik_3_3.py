import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys("FirstName")
browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys("LastName")
browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys("email@mail.com")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text is correct")

    def test_abs2(self):
        self.assertEqual(welcome_text, "Failed test", "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

time.sleep(2)
browser.quit()

