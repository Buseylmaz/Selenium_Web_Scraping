from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time



webDriver_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service_path=Service(webDriver_path)
driver=webdriver.Chrome(service=service_path)

driver.maximize_window()

#driver.implicitly_wait(20) bir defa kurulur

''' 
    1. Implicitly wait (Gizli bekleme): Bu bekleme türü WebDriver nesnesinin bir özelliğidir ve o Webdriver nesnesi var olduğu sürece geçerli olacaktır. 
    WebDriver nesnesini oluşturduğumuzda driver.implicitly_wait(30) şeklinde belirteceğimiz bekleme tüm proje boyunca aktif olacaktır. 
    Şayet daha sonra yine driver.implicitly_wait(10) şeklinde deklare edersek Selenium öncekini yok sayacak ve artık 10 saniye bekleyecektir.
    Biz bir kere deklare ettikten sonra arka planda bizim için element bulurken hata vermeden önce belirttiğimiz süre kadar elementi bulmaya çalışacaktır. 
    Bu süre zarfında bulamazsa o zaman hata verecektir. 

    2. Explicit wait (Açıktan bekleme): Adından da anlaşılacağı gibi implicit wait için belirttiğimiz süre yetersiz kalabilir diye düşünürsek o 
    durumda farklı bir beklemeye ihtiyacımız olacak. Bu durumda belli bir şart sağlanana kadar beklememiz gerekecek. 
    Explicit wait element düzeyinde kullanılır ve her seferinde yeniden deklare etmek gerekir. 

    WebDriverWait(driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
    Bu sentaks, CLICK ME yazan buton sayfada var olana kadar 45 saniye bekleyecektir. 

    Expected conditions bize bir çok seçenek sunmakta. Expected_conditions sonrasında nokta yazdığınızda beklemek için seleniumun kullanabileceği şartları görebilirsiniz. 
'''


driver.get("https://pynishant.github.io/Selenium-python-waits.html")


tryit=driver.find_element(By.XPATH,"//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver,45).until(expected_conditions.presence_of_element_located((By.XPATH,"//button[contains(text(), 'CLICK ME')]")))
clickme=driver.find_element(By.XPATH,"//button[contains(text(), 'CLICK ME')]").click()


time.sleep(5)

