from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

webDriver_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service_path=Service(webDriver_path)
driver=webdriver.Chrome(service=service_path)
driver.maximize_window()

driver.get("https://tomspizzeria.b4a.app/")

''' 1. is_selected() şayet web element seçili ise True , aksi halde değilse False verecektir. 
    2. is_displayed() şayet web element sayfada kullanıcıya görünür durumda ise True, aksi halde False verecektir. 
    3. is_enabled() ise web element kullanıcının etkileşimine açıksa True, aksi halde False verecektir.   '''

''' 1. options: Dropdown içindeki seçenekleri bize web element listesi olarak verir
    2. first_selected_option: Dropdownda o anda seçili olan seçeceği verir
    3. select_by_visible_text: Kullanıcıya görünen metin ile istediğimiz seçeceği seçmemize yarar
    4. select_by_index: İstediğimiz seçeneğin indeksini (0'dan başlayan indeks) kullanarak istediğimiz sıradaki seçeceği seçmemize yarar.  '''

name=driver.find_element(By.ID,"musteri-adi").send_keys("Buse Yılmaz")

pizza_size=driver.find_element(By.CSS_SELECTOR,"input[value='Orta']").click()

kind_of_pizza1=driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
#print(kind_of_pizza1.is_selected)
kind_of_pizza1.click()

kind_of_pizza2=driver.find_element(By.CSS_SELECTOR,"input[value='mısır']").click()


pay_method=driver.find_element(By.ID,"odeme-tipi")
pay_method1=Select(pay_method)
type_of_pay=pay_method1.options

for type in type_of_pay:
    print(type.text)

pay_method1.select_by_visible_text("Kredi Kartı")

#driver.find_element(By.CSS_SELECTOR,"option[value='Kredi Kartı']").click()


pay=driver.find_element(By.ID,"siparis").click()

detail=driver.find_element(By.ID,"siparis-detay").text
print("Sipariş Detayı")
print(detail)


















time.sleep(5)