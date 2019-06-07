from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://google.com')
# elem = driver.find_element_by_id('lst-ib')
elem = driver.find_element(By.XPATH, '//*[@id="lst-ib"]')
time.sleep(5)
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)