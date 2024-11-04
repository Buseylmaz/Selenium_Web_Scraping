from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


webDriver_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service_path=Service(webDriver_path)
driver=webdriver.Chrome(service=service_path)

driver.maximize_window()


#isim zorunlu

#pizza boyutu zorunlu

#ödeme tipi zorunlu

def Siparis(name):
    driver.get("https://tomspizzeria.b4a.app/")

    driver.find_element(By.ID,"musteri-adi").send_keys(name)
    driver.find_element(By.CSS_SELECTOR,"input[value='Orta']").click()

    pay_method=driver.find_element(By.ID,"odeme-tipi")
    pay_method1=Select(pay_method)
    pay_method1.select_by_visible_text("Kredi Kartı")

    driver.find_element(By.ID,"siparis").click()

    detail=driver.find_element(By.ID,"siparis-detay").text
    print("Sipariş Detayı")
    print(detail)

    message=driver.find_element(By.ID,"mesaj").text
    return message


message=Siparis("")
if "Müşteri ismi girmediniz" in message:
    print("Lütfen isminizi giriniz:")
else:
    print("Müşteri ismi girildi")

message=Siparis("Buse")
if "Müşteri ismi girmediniz" in message:
    print("Lütfen isminizi giriniz:")
else:
    print("Müşteri ismi girildi")

driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)
driver.save_screenshot("B:/scaping/EkranGörüntüsü/AşagıPizzaSiparişEkranı.png")
time.sleep(2)
driver.execute_script("window.scrollBy(0,-200)","")
time.sleep(2)
driver.save_screenshot("B:/scaping/EkranGörüntüsü/YukarıPizzaSiparişEkranı.png")

time.sleep(5)