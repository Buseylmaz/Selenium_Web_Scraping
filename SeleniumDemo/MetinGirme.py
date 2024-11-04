import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

time_=10

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
drive=webdriver.Chrome(service=service)

drive.maximize_window()

print("-----------------DUCK DUCK GO TEST------------------------")

drive.get("https://www.duckduckgo.com")

aramaÇubugu=drive.find_element(By.ID,"searchbox_input")
aramaÇubugu.send_keys("buse")

aramaÇubugu.send_keys(Keys.ENTER)

time.sleep(time_)


print("-----------------GOOGLE TEST------------------------")

drive.get("https://www.google.com")

aramaKısmı=drive.find_element(By.ID,"APjFqb")
aramaKısmı.send_keys("Selenium")

aramaKısmı.send_keys(Keys.ENTER)

time.sleep(time_)


