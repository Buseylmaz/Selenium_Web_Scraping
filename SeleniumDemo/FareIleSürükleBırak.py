from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
driver=webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://demoqa.com/droppable/")

driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)

kaynak=driver.find_element(By.CSS_SELECTOR,"div#simpleDropContainer div")
hedef=driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div.drop-box")

print("Önce: " + hedef.text)

action= ActionChains(driver)
action.drag_and_drop(kaynak,hedef).perform()

time.sleep(5)
print("Sonra: " + hedef.text)
time.sleep(2)













