import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


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
    # alert.dismiss()
    time.sleep(2)
    driver.switch_to.default_content()
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
    # alert.dismiss()
    driver.switch_to.default_content()  # --- to get back to browser from alert pop-up
    text = driver.find_element(By.ID, 'demo')
    print(text.text)
    time.sleep(2)
    driver.close()


if __name__ == '__main__':
    # switch_js_alert()
    switch_js_input_alert()
