"""
This pop-up /alert is not belongs to java script

we can pass the authentication credentials like (https://{}:{}@link..)
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth/')
