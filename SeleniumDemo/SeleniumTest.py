from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service=Service("B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service)

#Youtube sayfası için
driver.maximize_window()
driver.get("https://www.youtube.com/")
link=driver.current_url
baslik=driver.title
if "youtube.com" in link:
    print("Youtube sayfasi: "+link)
    print("Youtube Sayfa Basligi:" + " " +baslik)

print("------------------------------")

#Linkedin sayfası için 
driver.get("https://www.linkedin.com/")
link=driver.current_url
baslik=driver.title
if "linkedin.com" in link:
    print("Linkedin Sayfasi: "+link)
    print("Linkedin Sayfa Basligi:" + " " +baslik)

print("----------------------")

driver.back()
link=driver.current_url
baslik=driver.title
driver.save_screenshot("B:/scaping/EkranGörüntüsü/ekranGörüntüsü.png")
if "youtube.com" in link:
    print("Basarili,Youtube sayfasında ")
else:
    driver.save_screenshot("B:/scaping/EkranGörüntüsü/hataliEkranGörüntüsü.png")

#Şuan ki pencereyi kapat driver.close()

#Selenium kullandığı tüm pencereleri kapatır
driver.quit()


