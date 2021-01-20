"""
find_element - Returns first matching element
find_elements - Returns more than one element

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.amazon.in/')

# --- Elements
elements = driver.find_elements(By.TAG_NAME, 'a')
for i in elements:
    a = i.get_attribute('href')
    # print(i.get_attribute('href'))
print("print ELEMENTS length ::", len(a))

# --- Element
element = driver.find_element(By.TAG_NAME, 'a')
print("print ELEMENT tag ::", element.get_attribute('href'))
print("print ELEMENT Text ::", element.text)
