from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://londonfreelance.org/courses/frames/index.html')

# ----------- three ways we can pass the frame identification -------------

# --- frame 1
# driver.switch_to_frame(2)  # ---- By element
# driver.switch_to_frame('main')  # ---- By element
frame = driver.find_element(By.NAME, 'main')  # ---- Customised by element
driver.switch_to.frame(frame)

title = driver.find_element(By.TAG_NAME, 'h2')
print(title.text)

# --- frame 2
driver.switch_to.default_content()
driver.switch_to.frame('navbar')
title = driver.find_element(By.TAG_NAME, 'h3')
print(title.text)

# --- frame 1
driver.switch_to.default_content()
driver.switch_to.frame('main')
title = driver.find_element(By.TAG_NAME, 'h2')
print(title.text)
