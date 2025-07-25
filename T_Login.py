from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# Caminho correto para o executável
caminho_driver = r"C:\Users\Sena\OneDrive\Desktop\webdriver\chromedriver-win32\chromedriver.exe"
service = Service(caminho_driver)

driver = webdriver.Chrome(service=service)
driver.get("https://playful-torrone-162c28.netlify.app")
sleep(2)

login_button = driver.find_element(By.XPATH, '//span[text()="Login"]')
login_button.click()


sleep(10)
#driver.quit()
