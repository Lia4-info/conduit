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
from cond_data import *


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        # self.driver = webdriver.Chrome("C:\\Users\\Kornélia\\Desktop\\PM Automata Tesztelő\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://localhost:1667/")

    def teardown(self):
        self.driver.quit()

    # test 1 - accept cookies
    def test_accept_cookies(self):
        # self.driver.maximize_window()
        accept_btn = self.driver.find_element_by_xpath('//button[contains(@class,"accept")]')
        accept_btn.click()
        # assert self.driver.find_elements_by_xpath('//button') == []

    # test 2 - sign up
    def test_sign_up(self):
        sign_up_link = self.driver.find_element_by_xpath('//a[@href="#/register"]')
        sign_up_link.click()
        time.sleep(2)
        username_input = self.driver.find_element_by_xpath('//input[@placeholder="Username"]')
        username_input.send_keys("TKori103")
        email_input = self.driver.find_element_by_xpath('//input[@placeholder="Email"]')
        email_input.send_keys("tkori103@mail.com")
        password_input = self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
        password_input.send_keys("TKoriPass103")
        sign_up_btn = self.driver.find_element_by_xpath('//button[contains(text(),"Sign up")]')
        sign_up_btn.click()
        welcome = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "swal-title"))
        )
        assert welcome.text == "Welcome!"
        welcome_ok_btn = self.driver.find_element_by_xpath('//button[text()="OK"]')
        welcome_ok_btn.click()

    #test 3 - sign in
    # def test_sign_in(self):
    #     self.test_accept_cookies()
    #     sign_in_link = self.driver.find_element_by_xpath('//a[@href="#/login"]')
    #     sign_in_link.click()
    #     email_input = self.driver.find_element_by_xpath('//input[@placeholder="Email"]')
    #     password_input = self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
    #     email_input.send_keys("tkori103@mail.com")
    #     password_input.send_keys("TKoriPass103")
    #     sign_in_btn = self.driver.find_element_by_xpath('//button[contains(text(),"Sign in")]')
    #     sign_in_btn.click()
    #     user_signed_in = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"TKori")]'))
    #     )
    #     assert user_signed_in.is_displayed()

    # # test 4 - list artiles
    # def test_list_articles(self):
    #     self.test_sign_in()
    #     article_list = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//a[@class="preview-link"]'))
    #     )
    #     article_list = self.driver.find_elements_by_class_name("preview-link")
    #     assert article_list != []
    #
    # # test 5 - paginate
    # def test_paginate(self):
    #     self.test_sign_in()
    #     page_link2 = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//a[text()="2"]'))
    #     )
    #     page_link2.click()
    #     page2_check = self.driver.find_elements_by_xpath('//li[@data-test]')[1]
    #     assert page2_check.get_attribute("class") == "page-item active"
    #
    # # test 6 - save data into file
    # def test_save_data(self):
    #     self.test_sign_in()
    #     popular_tags = self.driver.find_elements_by_xpath('//div[a[@class="tag-pill tag-default"]]')
    #     with open('tags.csv', 'w', encoding="UTF-8") as tag_file:
    #         for tag in popular_tags:
    #             tag_file.write(tag.text)
    #             tag_file.write("\n")
    #
    # # test 7 - create new article
    # def test_create_article(self):
    #     self.test_sign_in()
    #     new_article_link = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//a[@href="#/editor"]'))
    #     )
    #     new_article_link.click()
    #     article_title = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]'))
    #     )
    #     article_about = self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]')
    #     article_text = self.driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
    #     enter_tags = self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]')
    #     publish_btn = self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]')
    #     article_title.send_keys(article1_title)
    #     article_about.send_keys(article1_about)
    #     article_text.send_keys(article1_text)
    #     for tag in article1_tags:
    #         enter_tags.send_keys(tag)
    #         enter_tags.send_keys(Keys.ENTER)
    #     publish_btn.click()
    #     # article1_url = "http://localhost:1667/#/articles/hello-world"
    #     # assert self.driver.current_url == article1_url
    #     article1_title_check = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//h1'))
    #     )
    #     assert article1_title_check.text == "Hello World!"
    #
    # # test 8 - add comments to article
    # def test_add_comments(self):
    #     self.test_create_article()
    #     comment_text = self.driver.find_element_by_xpath('//textarea[@placeholder="Write a comment..."]')
    #     post_comment_btn = self.driver.find_element_by_xpath('//button[text()="Post Comment"]')
    #     with open('comments.txt', 'r', encoding='UTF-8') as comments:
    #         for row in comments:
    #             comment_text.send_keys(row)
    #             post_comment_btn.click()
    #     comment_list = self.driver.find_elements_by_class_name("card-text")
    #     assert comment_list != []
    #
    #
    # # test 9 - delete article
    # def test_delete_article(self):
    #     self.test_create_article()
    #     delete_icon = self.driver.find_element_by_class_name("ion-trash-a")
    #     delete_icon.click()
    #     time.sleep(2)
    #     deleted_post_url = self.driver.current_url
    #     assert deleted_post_url == "http://localhost:1667/#/"
    #
    # # test 10 - edit profile_picture
    # def test_edit_profile_picture(self):
    #     self.test_sign_in()
    #     settings = self.driver.find_element_by_xpath('//a[@href="#/settings"]')
    #     settings.click()
    #     profile_picture_input = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="URL of profile picture"]'))
    #     )
    #     profile_picture_input.clear()
    #     profile_picture_input.send_keys("https://cdn.pixabay.com/photo/2019/02/19/19/45/thumbs-up-4007573__340.png")
    #     update_settings_btn = self.driver.find_element_by_xpath('//button[contains(text(),"Update Settings")]')
    #     update_settings_btn.click()
    #     update_succes = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "swal-title"))
    #     )
    #     assert update_succes.text == "Update successful!"
    #     update_ok_btn = self.driver.find_element_by_xpath('//button[text()="OK"]')
    #     update_ok_btn.click()
    #
    # # test 11 - logout
    def test_logout(self):
        conduit_sign_up(self.driver)
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ion-android-exit"))
        )
        logout_btn.click()
        sign_in_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@href="#/login"]'))
        )
        assert sign_in_link.is_displayed()
