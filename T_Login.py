from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Caminho correto para o executável
caminho_driver = r"C:\Users\Sena\OneDrive\Desktop\webdriver\chromedriver-win32\chromedriver.exe"
service = Service(caminho_driver)

driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

#Abrir Navegador e Site
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

#Clicar em '+ Criar Módulo'
criar_modulo_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.MuiButton-containedPrimary'))
)
criar_modulo_btn.click()

# Aguarda o campo "Título do Módulo" e preenche
titulo_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Título do Módulo"]')))
titulo_input.send_keys("Módulo Automatizado QA")


#--------------------------- INTERVALO
# Clica no dropdown de Série
serie_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="mui-component-select-grade"]')))
serie_dropdown.click()

# Aguarda a lista abrir e seleciona uma opção (ex: "3º Ano")
# Troque "3º Ano" pelo texto exato da opção desejada
serie_opcao = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[text()="3º Ano"]')))
serie_opcao.click()

# Preenche a descrição
descricao_input = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Descrição do Módulo"]')))
descricao_input.send_keys("Este é um módulo criado automaticamente via Selenium.")
#----------------------------- INTERVALO
sleep(10)
#driver.quit()
