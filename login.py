from selenium import webdriver
import pickle
import time
import os

from select_bar import *
import msg


#login function
def login(driver, character):
    URL = f'https://s{character.server}-{character.domain}.gladiatus.gameforge.com/game/'
    driver.get(URL)

    #load old cookies
    if os.path.exists(os.path.join(os.getcwd(),'cookies')):
        msg.info('Loading cookies...')
        with open("cookies", "rb") as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        msg.info('done')
        #time.sleep(1) 

    username_bar = select_bar.username(driver)
    password_bar = select_bar.password(driver)

    if (username_bar or password_bar) == False:
        msg.info("Already logged in!")
        return False

    msg.info("Logging in...")
    username_bar.send_keys(character.name)
    password_bar.send_keys(character.password)
    driver.find_element_by_id("loginsubmit").click()
    msg.info('done')

    #save cookies
    msg.info('Saving cookies...')
    with open('cookies', 'wb') as outfile:
        pickle.dump(driver.get_cookies(), outfile)
    msg.info('done')

    return True