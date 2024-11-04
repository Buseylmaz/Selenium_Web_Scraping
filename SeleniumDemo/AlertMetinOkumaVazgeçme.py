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

driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

button2=driver.find_element(By.XPATH,"(//button)[2]").click()

WebDriverWait(driver,3).until(expected_conditions.alert_is_present())

alert=Alert(driver)
time.sleep(2)
mesaj=alert.text
print(mesaj)

alert.dismiss()

result=driver.find_element(By.ID,"result").text
print(result)


button3=driver.find_element(By.XPATH,"(//button)[3]").click()

Alert(driver).send_keys("Buse")
Alert(driver).accept()

result=driver.find_element(By.ID,"result").text
print(result)


time.sleep(5)