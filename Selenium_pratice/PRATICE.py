from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def xpath_types():
    a = 1
    service = Service(executable_path=ChromeDriverManager().install())
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=opt)
    driver.get('https://www.amazon.in/')
    assert a == 1


if __name__ == '__main__':
    xpath_types()
