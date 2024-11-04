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