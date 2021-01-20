import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def switch_to_new_tab():
    """ ---------------------- Switch to new tab ------------------------------- """
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.amazon.in/')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.flipkart.com/')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()


def switch_browser_alert():
    """ ---------------------- Switch to frame ------------------------------- """
    option = Options()
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option('prefs', {"profile.default_content_setting_values.notifications": 1})

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)
    driver.maximize_window()
    driver.get('https://mercury.lawyer/login')
    time.sleep(5)
    driver.close()


def switch_js_alert():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('file:///home/vinod/PythonFrameWorkNew/Interview_Question_Examples/data_to_examples/js_alert.html')

    driver.find_element(By.XPATH, '//button[text()="Click Me"]').click()
    # alert = driver.switch_to_alert()
    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(2)
    alert.accept()
    time.sleep(2)
    driver.close()


def switch_js_input_alert():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('file:///home/vinod/PythonFrameWorkNew/Interview_Question_Examples/data_to_examples/js_input_alert.html')

    driver.find_element(By.XPATH, '//button[text()="Click Me"]').click()
    # alert = driver.switch_to_alert()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.send_keys("vinod")
    time.sleep(2)
    alert.accept()
    driver.switch_to.default_content()  # --- to get back to browser from alert pop-up
    text = driver.find_element(By.ID, 'demo')
    print(text.text)
    time.sleep(2)
    driver.close()


if __name__ == '__main__':
    # switch_to_new_tab()
    # switch_browser_alert()
    # switch_js_alert()
    switch_js_input_alert()
