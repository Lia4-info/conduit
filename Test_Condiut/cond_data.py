import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from article_generator import article1_title, article1_about, article1_text, article1_tags
from selenium.webdriver.common.keys import Keys

def driver_wait(driver, by, value):
    element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((by, value))
        )
    return element

def conduit_sign_up(driver):
    sign_up_link = driver.find_element_by_xpath('//a[@href="#/register"]')
    sign_up_link.click()

    username_input = driver.find_element_by_xpath('//input[@placeholder="Username"]')
    email_input = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    password_input = driver.find_element_by_xpath('//input[@placeholder="Password"]')
    sign_up_btn = driver.find_element_by_xpath('//button[contains(text(),"Sign up")]')

    username_input.send_keys("TKori103")
    email_input.send_keys("tkori103@mail.com")
    password_input.send_keys("TKoriPass103")
    sign_up_btn.click()
    welcome_ok_btn = driver_wait(driver, By.XPATH, '//button[text()="OK"]')
    welcome_ok_btn.click()

def conduit_sign_in(driver):
    sign_in_link = driver.find_element_by_xpath('//a[@href="#/login"]')
    sign_in_link.click()
    email_input = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    password_input = driver.find_element_by_xpath('//input[@placeholder="Password"]')
    email_input.send_keys("tkori103@mail.com")
    password_input.send_keys("TKoriPass103")
    sign_in_btn = driver.find_element_by_xpath('//button[contains(text(),"Sign in")]')
    sign_in_btn.click()

def conduit_logout(driver):
    conduit_sign_up(driver)
    logout_btn = driver_wait(driver, By.XPATH, '//*[@class="nav-link" and contains(text(),"Log out")]')
    logout_btn.click()

def conduit_new_article(driver):
    new_article_link = driver_wait(driver, By.XPATH, '//a[@href="#/editor"]')
    new_article_link.click()
    article_title = driver_wait(driver, By.XPATH, '//input[@placeholder="Article Title"]')
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