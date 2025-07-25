from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# Caminho correto para o executável
caminho_driver = r"C:\Users\Sena\OneDrive\Desktop\webdriver\chromedriver-win32\chromedriver.exe"
service = Service(caminho_driver)

#Abrir Navegador e Site
driver = webdriver.Chrome(service=service)
driver.get("https://playful-torrone-162c28.netlify.app")
sleep(2)

#Clicar em LOGIN
login_button = driver.find_element(By.XPATH, '//span[text()="Login"]')
login_button.click()

# Preenche os campos de login
driver.find_element(By.NAME, "email").send_keys("qualityassurance@bertoni.com.br")
driver.find_element(By.NAME, "password").send_keys("versar123")

#Efetua o Login e entra na página
driver.find_element(By.TAG_NAME, "form").submit()


sleep(10)
#driver.quit()
