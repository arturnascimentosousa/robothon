    try:
        btn_last_year = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-3')))
        btn_last_year.click()
    except StaleElementReferenceException:
        # Recarregar o elemento e tentar novamente
        btn_last_year = wait.until(EC.element_to_be_clickable((By.ID, 'newPerformanceCard-tab-3')))
        btn_last_year.click()
    
    print("Relatório do ano passado")
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'go2549335548')

    for i, element in enumerate(elements, start=1):
        element_text = element.text
        print(f"Element {i}: {element_text}")