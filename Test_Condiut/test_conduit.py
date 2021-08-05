import time
import pytest
from selenium import webdriver
from datetime import datetime
from email_generator import username, email, password
from article_generator import article1_title, article1_about, article1_text, article1_tags
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        # self.driver = webdriver.Chrome("C:\\Users\\Kornélia\\Desktop\\PM Automata Tesztelő\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://localhost:1667/")

    def teardown(self):
        self.driver.quit()

    # test1 - accept cookies
    def test_accept_cookies(self):
        self.driver.maximize_window()
        accept_btn = self.driver.find_element_by_xpath('//button[contains(@class,"accept")]')
        time.sleep(1)
        accept_btn.click()
        time.sleep(2)

    # test2 - sign up
    # def test_sign_up(self):
    #     self.test_accept_cookies()
    #     sign_up_link = self.driver.find_element_by_xpath('//a[@href="#/register"]')
    #     time.sleep(2)
    #     sign_up_link.click()
    #     time.sleep(2)
    #     username_input = self.driver.find_element_by_xpath('//input[@placeholder="Username"]')
    #     username_input.send_keys(username)
    #     email_input = self.driver.find_element_by_xpath('//input[@placeholder="Email"]')
    #     email_input.send_keys(email)
    #     password_input = self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
    #     password_input.send_keys(password)
    #     sign_up_btn = self.driver.find_element_by_class_name("btn btn-lg btn-primary pull-xs-right")
    #     sign_up_btn.click()
    #     time.sleep(2)
    #     welcome = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "swal-title"))
    #     )
    #     assert welcome.text == "Welcome!"
    #     welcome_ok_btn = self.driver.find_element_by_xpath('//button[text()="OK"]')
    #     welcome_ok_btn.click()
    #     time.sleep(2)

    def test_sign_in(self):
        self.test_accept_cookies()
        sign_in_link = self.driver.find_element_by_xpath('//a[@href="#/login"]')
        sign_in_link.click()
        email_input = self.driver.find_element_by_xpath('//input[@placeholder="Email"]')
        password_input = self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
        email_input.send_keys("tk1709@mail.com")
        password_input.send_keys("TKpass1709")
        sign_in_btn = self.driver.find_element_by_xpath('//button[contains(text(),"Sign in")]')
        sign_in_btn.click()

    # def test_logout(self):
    #     self.test_sign_in()
    #     logout_btn = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "ion-android-exit"))
    #     )
    #     logout_btn.click()
