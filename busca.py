from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#
# title = driver.title
#
# driver.implicitly_wait(0.5)
#
# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
# text_box.send_keys("Selenium")
# submit_button.click()
#
# message = driver.find_element(by=By.ID, value="message")
# text = message.text

empresa = "22896431000110"
driver.get(f"https://www.reclameaqui.com.br/busca/?q={empresa}")
score = driver.find_element(by=By.CLASS_NAME, value="score-search")
nome = driver.find_element(by=By.CLASS_NAME, value="title-company-card")

print(f"Nome: {nome.text}")
print(f"Score: {score.text}")

driver.quit()
