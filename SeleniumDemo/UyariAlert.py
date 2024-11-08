from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
import time


webDriver_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service_path=Service(webDriver_path)
driver=webdriver.Chrome(service=service_path)

driver.maximize_window()

driver.get("https://pynishant.github.io/Selenium-python-waits.html")


tryit=driver.find_element(By.XPATH,"//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver,45).until(expected_conditions.presence_of_element_located((By.XPATH,"//button[contains(text(), 'CLICK ME')]")))
clickme=driver.find_element(By.XPATH,"//button[contains(text(), 'CLICK ME')]").click()

WebDriverWait(driver,3).until(expected_conditions.alert_is_present())

uyari=Alert(driver)
uyari.accept()

time.sleep(5)