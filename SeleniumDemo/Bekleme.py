from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time



webDriver_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service_path=Service(webDriver_path)
driver=webdriver.Chrome(service=service_path)

driver.maximize_window()

#driver.implicitly_wait(20) bir defa kurulur

driver.get("https://pynishant.github.io/Selenium-python-waits.html")


tryit=driver.find_element(By.XPATH,"//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver,45).until(expected_conditions.presence_of_element_located((By.XPATH,"//button[contains(text(), 'CLICK ME')]")))
clickme=driver.find_element(By.XPATH,"//button[contains(text(), 'CLICK ME')]").click()


time.sleep(5)

