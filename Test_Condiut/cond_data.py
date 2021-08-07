import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    time.sleep(3)
    welcome_ok_btn = driver.find_element_by_xpath('//button[text()="OK"]')
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
    logout_btn = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//i[@class="ion-android-exit"]'))
    )
    logout_btn.click()