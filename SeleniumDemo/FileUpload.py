''' Testlerini otomasyon yaptığınız yazılım veya otomasyon yapıp vakit kazanmak istediğiniz bir rutin iş dosya yükleme içeriyorsa 
    python ve selenium ile bunu başarmak oldukça kolay. 

    Selenium ve python ile işletim sisteminin açtığı dosya bulma penceresini bypass ederek yükleyeceğimiz dosyanın 
    mutlak yerini (absolute path) send_keys fonksiyonu ile gönderebiliriz.

    Burada dikkat edilmesi gereken nokta, send_keys fonksiyonunu kullanacağımız web elementi doğru tespit etmek. 
    Etkileşime geçeceğimiz web element input olmalı ve type attribute değeri file olmalı ki bu web elementin dosya yükleme elementi olduğundan emin olalım. 

    NOT: File upload işlemleri vakit alacağı için 'yükle' benzeri butonlara tıkladıktan sonra explicit wait koymayı  unutmayın.
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
drive=webdriver.Chrome(service=service)

drive.maximize_window()
drive.implicitly_wait(30)

drive.get("https://the-internet.herokuapp.com/upload")

file="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"

upload_file=drive.find_element(By.ID,"file-upload")
time.sleep(2)
upload_file.send_keys(file)

upload_button=drive.find_element(By.ID,"file-submit").click()

WebDriverWait(drive,10).until(expected_conditions.presence_of_element_located((By.TAG_NAME,"h3")))

baslik=drive.find_element(By.TAG_NAME,"h3").text

print("baslik: ",baslik)

dosya=drive.find_element(By.ID,"uploaded-files").text

print("Dosya: ",dosya)

time.sleep(2)

drive.quit()