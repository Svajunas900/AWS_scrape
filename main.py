from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

url = "https://docs.aws.amazon.com/?nc2=h_ql_doc_do"

driver.get(url)


element = driver.find_element(by=By.XPATH, 
                              value="""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]
                              /div/section[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/h5/a""")
counter = 2
while element:
  try:
    print(element.text)
    element = driver.find_element(by=By.XPATH, 
                                  value=f"""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]
                                  /div/section[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[{counter}]/div/h5/a""")
    counter += 1
  except NoSuchElementException:  
    print("No such an element")
    break

print(element.text)

driver.quit()