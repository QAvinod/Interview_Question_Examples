from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()

right_click = driver.find_element(By.CSS_SELECTOR, '.btn-neutral')

action = ActionChains(driver)
action.context_click(right_click).perform()

elements = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon')
for i in elements:
    print(i.text)
    if i.text == 'Edit':
        i.click()
        break

alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.close()
