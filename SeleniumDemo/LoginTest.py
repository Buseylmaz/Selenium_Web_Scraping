import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

file_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service=Service(file_path)
drive=webdriver.Chrome(service=service)
drive.maximize_window()

#Assert ile yaptıgımız işlemi if else ile de yapabiliyoruz assert kod satırlarını azaltır iş yükünü azaltır ama bu yöntemi kullanmayacagız çünkü bir yerde hata varsa direk durduruyır ve kalanlara bakmıyor

def Login(username,password):
    drive.get("https://the-internet.herokuapp.com/login")
    drive.find_element(By.ID,"username").send_keys(username)
    drive.find_element(By.ID,"password").send_keys(password)

    drive.find_element(By.CLASS_NAME,"radius").click()

    message=drive.find_element(By.ID,"flash-messages").text
    return message

#Yanlış Şifre-Yanlış Kullanıcı Adı
message=Login("test1","123456")

assert "Your username is invalid!" in message

'''if "Your username is invalid!" in message:
    print("Kullanıcı adı yanlış şifre yanlış")
else:
    print("Error...")'''



#Dogru Şifre-Yanlış Kullanıcı Adı
message=Login("test","SuperSecretPassword!")

assert "Your username is invalid!" in message

'''if "Your username is invalid!" in message:
    print("Kullanıcı adı yanlış şifre dogru")
else:
    print("Error...")'''



#Dogru Kullanıcı Adı-Yanlış Şifre
message=Login("tomsmith","SuperSecretPassword")

assert "Your password is invalid!" in message

'''if "Your password is invalid!" in message:
    print("Kullanıcı adı dogru şifre yanlış")
else:
    print("Error...")'''



#Dogru Kullanıcı Adı-Dogru Şifre
message=Login("tomsmith","SuperSecretPassword!")

assert "You logged into a secure area!" in message

'''if "You logged into a secure area!" in message:
    print("Kullanıcı adı dogru şifre dogru")
else:
    print("Error...")'''


time.sleep(2)



