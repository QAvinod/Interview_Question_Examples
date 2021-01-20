from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
driver.maximize_window()

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

action = ActionChains(driver)

# ------ drag and drop
# action.drag_and_drop(source, target).perform()


# ------ left click hold and drag and drop
action.click_and_hold(source).move_to_element(target).release().perform()
