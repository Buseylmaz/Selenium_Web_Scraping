from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"

options=Options()

options.add_experimental_option("excludeSwitches", ["enable-automation"]) #otomosyon aktive eder
options.add_experimental_option('useAutomationExtension', False) #otomosyon aktive eder
options.add_argument("--disable-infobars") #ayukarda ki açıklamayı kapatır
options.add_argument("--allow-running-insecure-content") #gelen uyarıları kapatır-güvenlik ile
options.add_argument("--disable-notifications") #javascrit alert benzeyen uyarıları kapatır
options.add_argument("--disable-save-password") #şifre kaydetme kapatır
options.add_argument("--disable-extensions") #
options.add_argument("download.default_directory=C:/kullanicilar/ali/test") #indirilen dosya yerini değiştirir
options.add_argument("--window-size=768,1024") #
options.add_argument("--disable-popup-blocking") #popup kapatır

service=Service(file_path)
driver=webdriver.Chrome(service=service , options=options)

#driver.maximize_window()

driver.get("https://www.google.com/")

time.sleep(5)