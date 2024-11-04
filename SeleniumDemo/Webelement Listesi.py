from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


webDriver_path="B:/scaping/SeleniumDemo/chromedriver-win64/chromedriver.exe"
service_path=Service(webDriver_path)
driver=webdriver.Chrome(service=service_path)
driver.get("https://duckduckgo.com")
driver.maximize_window()


search=driver.find_element(By.ID,"searchbox_input").send_keys("imdb")

search_button=driver.find_element(By.CLASS_NAME,"searchbox_iconWrapper__suWUe").click()

find_site=driver.find_element(By.ID,"r1-0").click()

find_imdb_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "imdbHeader-navDrawerOpen"))).click()

find_top_movies=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Top 250 Movies']"))).click()

film_name=driver.find_elements(By.CLASS_NAME,"ipc-title-link-wrapper")
film_year=driver.find_elements(By.XPATH,"//span[@class='sc-5bc66c50-6 OOdsw cli-title-metadata-item']")



time.sleep(5)