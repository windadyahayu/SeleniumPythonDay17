import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from data import datanya
from page import locator


class TestLoginRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_Negatif(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys(
            "Salah")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            "salah")  # isi password
        time.sleep(1)
        # driver.find_element(By.ID, "btnLogin").click()
        driver.find_element(By.ID, "login-button").click()

        response_message = driver.find_element(
            By.CSS_SELECTOR, locator.alert).text
        self.assertEqual(
            response_message, datanya.errormessage)


unittest.main()
