import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
drive=webdriver.Chrome(service=service)

drive.maximize_window()

link=drive.get("https://tr.wikipedia.org/wiki/Anasayfa")
seckin_madde_hücresi=drive.find_element(By.ID,"mp-itn")
seckin_madde_metni=seckin_madde_hücresi.text
seckin_madde_metni=seckin_madde_metni.split(":")[0]
print(seckin_madde_metni)

#time.sleep(5)