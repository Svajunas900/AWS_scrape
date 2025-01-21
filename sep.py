from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = "https://docs.aws.amazon.com/?nc2=h_ql_doc_do"

driver.get(url)
element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]/div/section[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/h5/a"))
    )
element.click()

element2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]/div/section[1]/div/div/div/div/div/div/ol/li[3]/div/div[1]/div/h3/span/a/span"))
    )
element2.click()
driver.implicitly_wait(1)
driver.quit()