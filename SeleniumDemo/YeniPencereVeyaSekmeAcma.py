''' WebDriver nesnemiz (driver adını verdiğimiz değişken) ile driver.switch_to.window(hint) yazarak yeni bir sekme veya pencere açabiliriz. 
    Burada hint bir string değeri. Şayet parantez içine "tab" yazarsak yeni bir sekme,  "window" yazarsak yeni bir pencere açılacaktır.
'''
''' Gündelik hayatımızda internette gezinirken çoğumuz aynı anda bir chrome veya firefox penceresinde birden fazla sekme ile çalışırız. 
    Aynı anda bir çoğumuzda yarım düzine sekme açıktır. 
    Bizler sekme başlığına bakarak istediğimiz sekmeye geçiyoruz çünkü bir sekmede iken diğer sekmelerde bir işlem yapamayız. 
    Peki bunu selenium ve python kullanarak nasıl yapacağız?

    WebDriver nesnemiz açtığı her bir sekme/pencere için harf ve rakamlardan oluşan rastgele bir window_handle (o sekmeye özgü bir tür kullanıcı adı)  oluşturacaktır. 
    Bu window_handle değerlerini kullanarak istediğimiz sekmeye geçiş yapabiliriz. 
    WebDriver (driver adını verdiğimiz değişken) ile driver.current_window_handle bize şuan driver nesnemizin aktif olduğu sekmenin window_handle ını verecektir. 
    Öte yandan driver.window_handles ise driver nesnemizin kontrol edebileceği tüm sekmelerin window_handle larını verecektir. 

    Bu window_handle değerlerini kullanarak driver.switch_to.window(parametre) yazarak ve parametre yerine string olarak girdiğimiz window_handle sekmesine geçiş yapabiliriz.
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
drive=webdriver.Chrome(service=service)

drive.maximize_window()
drive.implicitly_wait(30)

#drive.switch_to.new_window("tab")
#drive.switch_to.new_window("window")

drive.get("https://www.apple.com")
print(drive.title)
apple=drive.current_window_handle
print("Apple: ", drive.current_window_handle)

time.sleep(3)

drive.switch_to.new_window("tab")
drive.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
print(drive.title)
print("Crummy: " , drive.current_window_handle)

print("List Window Handles:" , drive.window_handles)

time.sleep(2)
drive.switch_to.window(apple) #ilk önce apple sekmesi açıcak sonra curmmy sekmesine geçecek bu kodlada tekrar apple sekmesine gelecek

time.sleep(2)