import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException




# Função para buscar o nome da empresa via API pelo CNPJ
def get_company_name_by_cnpj(cnpj):
    url = f"https://open.cnpja.com/office/{cnpj}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
        
        # Converte a resposta JSON em um dicionário Python
        company_data = response.json()
        company_name = company_data['company']['name']
        print(f"Company Name: {company_name}")
        print(f"CNPJ: {company_data.get('cnpj')}")
        return company_name
        
    except requests.exceptions.RequestException as e:
        print(f"Error accessing API: {e}")
        return None
    except ValueError:
        print("Error converting response to JSON")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Função para pesquisar no Google e capturar elementos com Selenium
def search_company_in_reclame_aqui(company_name):
    if not company_name:
        print("Invalid company name")
        return
    
    # Pesquisa no Google "nome_da_empresa reclame aqui"
    search_query = f"{company_name} reclame aqui"
    url_search = f"https://www.google.com/search?q={search_query}"

    # Configura o WebDriver (substitua o caminho para o ChromeDriver se necessário)
    driver = webdriver.Chrome()  # ou webdriver.Firefox() para Firefox
    driver.get(url_search)

    # Espera um pouco para garantir que a página carregou
    time.sleep(3)

    # Clica no primeiro link dos resultados da pesquisa
    first_link = driver.find_element(By.CSS_SELECTOR, 'h3')
    first_link.click()

    # Espera mais um pouco para a nova página carregar
    time.sleep(5)

    # Captura todos os elementos com a classe "go2549335548"
    elements = driver.find_elements(By.CLASS_NAME, 'go2549335548')

    # Itera sobre os elementos e imprime cada um deles com o padrão solicitado
    print("\nRelatório dos últimos 6 meses")
    for i, element in enumerate(elements, start=1):
        element_text = element.text
        print(f"Element {i}: {element_text}")
    
    element_avg_notes = driver.find_element(By.CLASS_NAME, 'go1306724026')
    print(element_avg_notes.text)

    print("Tipos de problema")


    
    wait = WebDriverWait(driver, 10)

# Envolva o clique em um bloco try-except para lidar com o StaleElementReferenceException
    try:
        btn12month = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-2')))
        btn12month.click()
    except StaleElementReferenceException:
        # Recarregar o elemento e tentar novamente
        btn12month = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-2')))
        btn12month.click()


    print("\nRelatório dos últimos 12 meses")
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'go2549335548')

    for i, element in enumerate(elements, start=1):
        element_text = element.text
        print(f"Element {i}: {element_text}")
    
    element_avg_notes = driver.find_element(By.CLASS_NAME, 'go1306724026')
    print(element_avg_notes.text)

    try:
        btn_last_year = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-3')))
        btn_last_year.click()
    except StaleElementReferenceException:
        # Recarregar o elemento e tentar novamente
        btn_last_year = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-3')))
        btn_last_year.click()
    
    print("\nRelatório do ano passado")
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'go2549335548')

    for i, element in enumerate(elements, start=1):
        element_text = element.text
        print(f"Element {i}: {element_text}")
    
    element_avg_notes = driver.find_element(By.CLASS_NAME, 'go1306724026')
    print(element_avg_notes.text)

    try:
        btn_before_last_year = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-4')))
        btn_before_last_year.click()
    except StaleElementReferenceException:
        # Recarregar o elemento e tentar novamente
        btn_before_last_year = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-4')))
        btn_before_last_year.click()
    
    print("\nRelatório do ano retrasado")
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'go2549335548')

    for i, element in enumerate(elements, start=1):
        element_text = element.text
        print(f"Element {i}: {element_text}")
    
    element_avg_notes = driver.find_element(By.CLASS_NAME, 'go1306724026')
    print(element_avg_notes.text)
    
    try:
        btn_infos_geral = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-5')))
        btn_infos_geral.click()
    except StaleElementReferenceException:
        # Recarregar o elemento e tentar novamente
        btn_infos_geral = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-5')))
        btn_infos_geral.click()
    
    print("\nRelatório geral")
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'go2549335548')

    for i, element in enumerate(elements, start=1):
        element_text = element.text
        print(f"Element {i}: {element_text}")
    
    element_avg_notes = driver.find_element(By.CLASS_NAME, 'go1306724026')
    print(element_avg_notes.text)
    # Fecha o navegador
    driver.quit()

# Exemplo de uso
cnpj = "00000000000191"  # Substitua pelo CNPJ desejado
company_name = get_company_name_by_cnpj(cnpj)
search_company_in_reclame_aqui(company_name)
