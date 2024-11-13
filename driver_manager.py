from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def restart_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    return driver, wait
