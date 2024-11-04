''' 
    Bazen web sitelerinde kullanıcıya sunulan seçenekler çok fazla olunca yazılımcılar dinamik dropdown, 
    diğer adıyla suggestive search, kullanırlar. Bunlar HTML ile select tag kullanılmadığı için Select class kullanarak otomasyon yapamayız.
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
driver=webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://www.ucuzabilet.com/")

driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)


nereye=driver.find_element(By.ID,"from_text").send_keys("Avust")
time.sleep(2)

yer=driver.find_element(By.XPATH,"//li[contains(text(), 'GRZ')]").click()
time.sleep(2)
print("Başarılı")



