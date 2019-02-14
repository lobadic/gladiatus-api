


import character
from select_bar import *

from selenium import webdriver
import pickle
import time
import os
import msg

from login import *
from complete_movements import *



driver = webdriver.Chrome()
login(driver, character)


goto_country(driver)
time.sleep(1)
goto(select_bar.event_zone(driver))





while True:
    time.sleep(60)