''' 
    Web sitelerinde gezinirken bazen bir metni görmek veya bir linki tıklamak için faremizi bir elementin üzerine getirmemiz gerekir. 
    Şimdiye kadarki derslerde fare ile tıklama nasıl yapılır öğrendiniz. 
    Ancak bu durumda herhangi bir tıklama yapmadan sadece fareyi belirli bir noktaya oynatıp durmamız gerekiyor. 
    Bu eylem için selenium bize ActionChains class ını veriyor. Bu class içindeki move_to_element fonksiyonu, fareyi vereceğimiz bir webelementin üzerine hareket ettirecektir. 

    Ekranda kodunuzun çalışmasını izlerken farenin hareket etmediğini görebilirisiniz. Selenium fareyi fiziksel olarak oynatmayacak, 
    farenin arka planda yaptığı işlemi yapacaktır. 
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
driver=webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/hovers")

user=driver.find_element(By.CSS_SELECTOR,"div.figure")
name=driver.find_element(By.CSS_SELECTOR,"div.figcaption h5")
link=driver.find_element(By.CSS_SELECTOR,"div.figcaption a")

print(name.is_displayed())
print("İsim: " +name.text)

time.sleep(2)

hareket=ActionChains(driver)
hareket.move_to_element(user)
hareket.perform() #kullanılması zorunlu

time.sleep(2)

print("---------")
print(user.is_displayed())
print("İsim: " +name.text)
link.click()

time.sleep(2)

url=driver.current_url

assert "users/1" in url
driver.quit()


