from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date, datetime


today = datetime.now()

driver = webdriver.Ie()
driver.get('https://mcf-portal.eslabs.ssn.hpe.com/login.aspx')
elem = driver.find_element_by_id('ContentPlaceHolder1_login1_UserName')
time.sleep(2)
elem.clear()
elem.send_keys('venkatesh.rathod@hpe.com')
time.sleep(2)
elem = driver.find_element_by_id('ContentPlaceHolder1_login1_Password')
time.sleep(2)
elem.send_keys('Venki@123')
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
print("-" * 70)
if "BPS Portal-Home" in driver.title:
 file1 = open('testfile.txt','a')
 print("\n------------------------------------------------\nLOGIN TEST -- PASSED. The page title is: '%s'||" % driver.title, today, file = file1)
 file1.close()
else:
  print("\n------------------------------------------------\nLOGIN TEST -- FAILED (or the page title has been changed to: '%s'.\n" % driver.title, today, file = file1)


elem = driver.find_element(By.CSS_SELECTOR,'.level1.static>li:nth-child(3)')
elem.click()
time.sleep(2)
print("-" * 70)
if "iDMS Home Page" in driver.title:
 file1 = open('testfile.txt','a')
 print("\n------------------------------------------------\niDMSLink was successful -- PASSED. The page title is: '%s'||" % driver.title, today, file = file1)
 file1.close()
else:
  print("\n------------------------------------------------\niDMSLink was -- FAILED (or the page title has been changed to: '%s'.\n" % driver.title, today, file = file1)


elem = driver.find_element(By.CSS_SELECTOR,'#CDMSLeftNavigation>li:nth-child(3)')
elem.click()
time.sleep(2)

print("-" * 70)
if "Help Document" in driver.title:
 file1 = open('testfile.txt','a')
 print("\n------------------------------------------------\n Help Document Link was successful -- PASSED. The page title is: '%s'||" % driver.title, today, file = file1)
 file1.close()
else:
  print("\n------------------------------------------------\nHelp Document Link was -- FAILED (or the page title has been changed to: '%s'.\n" % driver.title, today, file = file1)

driver.back()