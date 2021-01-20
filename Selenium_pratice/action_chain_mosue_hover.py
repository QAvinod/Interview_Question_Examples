import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.spicejet.com/')

sign_in = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
sign_in.click()

action = ActionChains(driver)
action.move_to_element(sign_in).perform()

spice_club = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
action.move_to_element(spice_club).perform()

login = driver.find_element(By.LINK_TEXT, 'Member Login')
login.click()

time.sleep(3)
driver.close()
