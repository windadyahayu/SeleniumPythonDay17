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

    def test_Checkout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys(datanya.nama)  # isi email
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys(
            datanya.password)  # isi password
        time.sleep(3)
        # driver.find_element(By.ID, "btnLogin").click()
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        driver.find_element(
            By.CSS_SELECTOR, "#item_4_title_link > div").click()
        time.sleep(5)
        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        time.sleep(3)
        # remove
        driver.find_element(
            By.CSS_SELECTOR, "#remove-sauce-labs-backpack").click()
        time.sleep(3)
        driver.find_element(
            By.CSS_SELECTOR, "#header_container > div.header_secondary_container > div").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#item_0_img_link > img").click()
        time.sleep(3)
        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()
        time.sleep(5)

        driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        time.sleep(5)
        driver.find_element(By.ID, "first-name").send_keys("winda")
        time.sleep(3)
        driver.find_element(By.ID, "last-name").send_keys("dyahayu")
        time.sleep(3)
        driver.find_element(By.ID, "postal-code").send_keys("16320")
        time.sleep(5)
        driver.find_element(By.ID, "continue").click()
        time.sleep(3)
        driver.find_element(By.ID, "finish").click()
        time.sleep(5)


unittest.main()
