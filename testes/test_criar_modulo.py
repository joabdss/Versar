def test_criar_modulo():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from time import sleep

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://playful-torrone-162c28.netlify.app")
        sleep(2)

        driver.find_element(By.XPATH, '//span[text()="Login"]').click()
        driver.find_element(By.NAME, "email").send_keys("qualityassurance@bertoni.com.br")
        driver.find_element(By.NAME, "password").send_keys("versar123")
        driver.find_element(By.TAG_NAME, "form").submit()

        criar_modulo_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.MuiButton-containedPrimary')))
        criar_modulo_btn.click()

        titulo_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Título do Módulo"]')))
        titulo_input.send_keys("Módulo Automatizado QA")

        dropdown_btn = wait.until(EC.element_to_be_clickable((By.ID, "mui-component-select-grade_id")))
        dropdown_btn.click()
        opcao_serie = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//ul[@role="listbox"]//li[contains(translate(text(),"º°", ""), "3 ANO")]')
        ))
        opcao_serie.click()

        descricao_input = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Descrição do Módulo"]')))
        descricao_input.send_keys("Este é um módulo criado automaticamente via Selenium.")

        botao_estrela = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '(//li[@class="MuiGridListTile-root"]//button[@type="button"])[1]')
        ))
        botao_estrela.click()

        for _ in range(2):
            botao_salvar = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//button[.//span[contains(text(),"Salvar")]]')
            ))
            botao_salvar.click()

        botao_salvar_modulo = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[.//span[contains(text(),"Salvar Módulo")]]')
        ))
        botao_salvar_modulo.click()

        sleep(5)

        # Se chegou até aqui sem erro, o teste passou
        assert True

    except Exception as e:
        assert False, f"Erro no teste: {e}"

    finally:
        driver.quit()
