from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://www.fifa.com/")


time.sleep(2)