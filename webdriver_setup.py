from selenium import webdriver
import time

def setup_driver():
    # Setup the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("http://sdetchallenge.fetch.com")
    time.sleep(3)  # Ensure the page loads completely
    return driver
