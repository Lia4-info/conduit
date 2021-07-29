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

PATH = "C:\\Users\\Kornélia\\Desktop\\PM Automata Tesztelő\\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:1667/"
driver = webdriver.Chrome(PATH)

driver.get(URL)
accept_btn = driver.find_element_by_xpath('//button[contains(@class, "accept")]')
time.sleep(2)
accept_btn.click()
time.sleep(2)

# sign_up_link = driver.find_element_by_xpath('//a[@href="#/register"]')
# time.sleep(2)
# sign_up_link.click()
# time.sleep(2)
# username_input = driver.find_element_by_xpath('//input[@placeholder="Username"]')
# username_input.send_keys(username)
# email_input = driver.find_element_by_xpath('//input[@placeholder="Email"]')
# email_input.send_keys(email)
# password_input = driver.find_element_by_xpath('//input[@placeholder="Password"]')
# password_input.send_keys(password)
# sign_up_btn = driver.find_element_by_xpath('//button[contains(text(),"Sign up")]')
# sign_up_btn.click()
# welcome = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.CLASS_NAME, "swal-title"))
#         )
# assert welcome.text == "Welcome!"
# welcome_ok_btn = driver.find_element_by_xpath('//button[text()="OK"]')
# welcome_ok_btn.click()
# time.sleep(2)

# logout_btn = driver.find_element_by_class_name("ion-android-exit")
# logout_btn.click()

sign_in_link = driver.find_element_by_xpath('//a[@href="#/login"]')
sign_in_link.click()
email_input = driver.find_element_by_xpath('//input[@placeholder="Email"]')
password_input = driver.find_element_by_xpath('//input[@placeholder="Password"]')
email_input.send_keys("tk1709@mail.com")
password_input.send_keys("TKpass1709")
sign_in_btn = driver.find_element_by_xpath('//button[contains(text(),"Sign in")]')
sign_in_btn.click()

new_article_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@href="#/editor"]'))
        )
new_article_link.click()
time.sleep(2)
article_title = driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
article_about = driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]')
article_text = driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
enter_tags = driver.find_element_by_xpath('//input[@placeholder="Enter tags"]')
publish_btn = driver.find_element_by_xpath('//button[contains(text(),"Publish")]')
article_title.send_keys(article1_title)
article_about.send_keys(article1_about)
article_text.send_keys(article1_text)
for tag in article1_tags:
    enter_tags.send_keys(tag)
    enter_tags.send_keys(Keys.ENTER)

publish_btn.click()
time.sleep(2)
article1_url = "http://localhost:1667/#/articles/hello-world"
article1_title_check = driver.find_element_by_xpath('//h1')
assert article1_title_check.text == "Hello World!"

edit_icon = driver.find_element_by_class_name("ion-edit")
delete_icon = driver.find_element_by_class_name("ion-trash-a")
comment_text = driver.find_element_by_xpath('//textarea[@placeholder="Write a comment..."]')
post_comment_btn = driver.find_element_by_xpath('//button[text()="Post Comment"]')

page_link2 = driver.find_element_by_xpath('//a[text()="2"]')


# logout_btn = driver.find_element_by_class_name("ion-android-exit")
# logout_btn.click()



# settings = driver.find_element_by_xpath('//a[@href="#/settings"]')
# settings.click()
