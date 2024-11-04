''' Web sayfası veya web tabanlı yazılım geliştirirken nadir de olsa bazen yazılımı geliştirenlerin kullanıcıya bir takım uyarılar göndermesi gerekebilir.
    Test ettiğimiz veya testlerini otomasyon yaptığımız web yazılımları bu noktada bizlere farklı bir engel çıkartabilir. 
    Selenium için elementleri HTML ve CSS ile buluyoruz. 
    Ama javascript alert ler HTML içinde olmadığı için bunları locate edip selenium'un bize sunduğu click() fonksiyonunu kullanamayız. 

    Bu sorunu aşmak için seleniumu geliştirenler Alert() class ını bizlere sunuyor. 
    Alert() class ının bir nesnesini oluşturup WebDriver nesnemizi verdiğimizde alert nesnesi bizlere javascript alert ler ile etkileşime 
    geçmemize olanak sağlayacaktır. Bunun için:

    alert = Alert(driver) yazarak bir Alert() class nesnesi oluşturabiliriz. Sonrasında ise:
    alert.accept() fonksiyonu ile uyarıyı kabul edebiliriz. 

    JavaScript alert leri Evet/Hayır mantısı ile tasarlanır. 
    Diğer ifadeyle kullanıcı ya kabul edecektir veya etmeyecektir. 
    Dolayısıyla, işletim sistem dili ne olur olsun  mesajı kabul etmek için tek bir buton olacaktır. 
    Bu buton OK, Tamam, Kabul, Katılıyorum vs yazabilir. Ama tıklamak için accept() fonksiyonunu kullanabilirsiniz. 
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
import time


webDriver_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service_path=Service(webDriver_path)
driver=webdriver.Chrome(service=service_path)

driver.maximize_window()

driver.get("https://pynishant.github.io/Selenium-python-waits.html")


tryit=driver.find_element(By.XPATH,"//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver,45).until(expected_conditions.presence_of_element_located((By.XPATH,"//button[contains(text(), 'CLICK ME')]")))
clickme=driver.find_element(By.XPATH,"//button[contains(text(), 'CLICK ME')]").click()

WebDriverWait(driver,3).until(expected_conditions.alert_is_present())

uyari=Alert(driver)
uyari.accept()

time.sleep(5)