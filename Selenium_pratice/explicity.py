"""Explicitly wait -  As webdriver wait.
It has 19 ways to wait and check your
web element are visible/presence/clickable...etc.
Ex:- WebDriverWait(driver, 10)"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

results = ''


def browser():
    global results
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.find_element(By.ID, 'twotabsearchtextbox')
        results = True
    except Exception as error:
        print(error)

    if results:
        print('true')
        wait.until(ec.presence_of_element_located((By.ID, 'twotabsearchtextbox'))).click()


if __name__ == '__main__':
    browser()
