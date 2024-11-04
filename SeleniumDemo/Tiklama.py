import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
drive=webdriver.Chrome(service=service)

drive.maximize_window()


print("---------- DUCK DUCK GO TEST -------------")
drive.get("https://www.duckduckgo.com")

aramaTıklama=drive.find_element(By.ID,"searchbox_input")
aramaTıklama.send_keys("Selenium")

tikla=drive.find_element(By.CLASS_NAME,"searchbox_iconWrapper__suWUe")
tikla.click()

drive.find_element(By.ID,"r1-4").click()

time.sleep(5)

print("---------- GOOGLE TEST -------------")
drive.get("https://www.google.com")

arama=drive.find_element(By.ID,"APjFqb")
arama.send_keys("Selenium")

aramaTiklama=drive.find_element(By.CSS_SELECTOR,"div.FPdoLc input.gNO89b").click() #olmuyor çünkü arama kısmını bulamaıyor açılır kısımın altında kaldıgı için

#drive.find_element(By.CLASS_NAME,"1").click()

time.sleep(10)


