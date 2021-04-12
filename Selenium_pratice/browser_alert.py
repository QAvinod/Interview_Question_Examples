import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def browser_alert_view():
    """ ---------------------- Switch to frame ------------------------------- """
    option = webdriver.ChromeOptions()
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option('prefs', {"profile.default_content_setting_values.notifications": 3})
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)
    driver.maximize_window()
    driver.get('https://mercury.lawyer/login')
    time.sleep(5)
    driver.close()


def browser_alert_accept():
    """ ---------------------- Switch to frame ------------------------------- """
    option = webdriver.ChromeOptions()
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option('prefs', {"profile.default_content_setting_values.notifications": 1})
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)
    driver.maximize_window()
    driver.get('https://mercury.lawyer/login')
    time.sleep(5)
    driver.close()


def browser_alert_block():
    """ ---------------------- Switch to frame ------------------------------- """
    option = webdriver.ChromeOptions()
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option('prefs', {"profile.default_content_setting_values.notifications": 2})
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)
    driver.maximize_window()
    driver.get('https://mercury.lawyer/login')
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    browser_alert_view()
    browser_alert_accept()
    browser_alert_block()
