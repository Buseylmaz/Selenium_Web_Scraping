''' 
    Web yazılımlarını selenium ile otomasyon yaparken uzun vadede karşılaşılan sorunlardan birisi de 
    bilgisayardaki tarayıcı versiyonun projedeki driver ile uyuşmaması. Çünkü projeye driver dosyasını koyduktan sonra tarayıcının kendisi 
    birkaç kez güncellenmiştir. 

    Webdriver Manager bize bu sorunu aşmamıza yardım ediyor. 
    Kodumuz çalıştığında bu paket bilgisayarımızda yüklü tarayıcının versiyonuna bakıp internetten ona uyumlu dosyaları indiriyor. 
    Böylelikle bizim tarayıcı versiyon uyumunu dert etmemize gerek kalmıyor.
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://www.fifa.com/")


time.sleep(2)