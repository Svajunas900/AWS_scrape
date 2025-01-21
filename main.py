from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from functions import get_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = "https://docs.aws.amazon.com/?nc2=h_ql_doc_do"

driver.get(url)


aws_service_element = driver.find_element(by=By.XPATH, 
                              value="""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]
                              /div/section[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/h5/a""")
element_counter = 2

cookie = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/div/button[1]"))
    )
cookie.click()

while aws_service_element:
  try:
    get_element(driver, aws_service_element)
    driver.implicitly_wait(2)
    aws_service_element = driver.find_element(by=By.XPATH, 
                                  value=f"""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]
                                  /div/section[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[{element_counter}]/div/h5/a""")
    
    element_counter += 1
  except NoSuchElementException:  
    print("No such an aws_service_element")
    break

driver.quit()