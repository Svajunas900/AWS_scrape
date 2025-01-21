from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from functions import get_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = "https://docs.aws.amazon.com/?nc2=h_ql_doc_do"

driver.get(url)


element = driver.find_element(by=By.XPATH, 
                              value="""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]
                              /div/section[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/h5/a""")
counter = 2
cookie = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/div/button[1]"))
    )
cookie.click()
while element:
  try:
    print(element.text)
    get_element(driver,element)
    driver.implicitly_wait(2)
    element = driver.find_element(by=By.XPATH, 
                                  value=f"""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]
                                  /div/section[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[{counter}]/div/h5/a""")
    
    counter += 1
  except NoSuchElementException:  
    print("No such an element")
    break

print(element.text)




driver.quit()