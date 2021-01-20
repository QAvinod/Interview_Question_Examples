"""Implicitly wait - Works for WEB ELEMENTS.
and it is common wait function for whole
web elements in your file. and not support to.
title/.click/.sendkeys...etc.,"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Firefox(executable_path='')
    # driver = webdriver.Safari(executable_path='')
    # driver = webdriver.Ie(executable_path='')
    # driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    driver.get('https://www.amazon.in/')
    driver.maximize_window()

    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Implicit wait')
    driver.find_element(By.ID, 'nav-search-submit-button').click()


if __name__ == '__main__':
    browser()
