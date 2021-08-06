import time


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