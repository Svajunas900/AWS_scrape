from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decorators import decor


@decor
def write_to_file(file_name, text):
  with open(f"AWS_{file_name}.txt", 'a') as file:
    file.write(text + '\n')


def get_text(driver, counter):
  try:
    element = driver.find_elements(by=By.XPATH, value=f"""/html/body/div[2]/div/div/div[2]/main/div[3]/div/div[4]/div[1]/div/div/div/div[2]/div/div/div/div/div[4]/div[1]/p[{counter}]""")
  except NoSuchElementException:
    return None
  if element:
    return element[0].text
  else:
    return


def get_element(driver, element):
  root = str(element.text)
  element.click()
  try:
    element1 = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.XPATH, f"""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]/div/section[1]/div/div/div/div/div/div/ol/li[1]/div/div[1]/div/h3/span/a/span"""))
      )
  except NoSuchElementException:
    element1 = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.XPATH, f"""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]/div/section[1]/div[2]/div/div/div/div/div/ol/li[1]/div/div[1]/div/h3/span/a/span"""))
      )
  counter = 2
  text_counter = 1
  text = "Help"
  while element1:
    try:
      print(element1)
      element1.click()
      while text:
        text = get_text(driver, text_counter)
        write_to_file(root, str(text))
        text_counter += 1
      driver.back()
      driver.implicitly_wait(1)
      element1 = driver.find_element(by=By.XPATH, 
                            value=f"""/html/body/div[2]/div/div/div[2]/main/div[1]
                            /div/div[1]/div[4]/div/section[1]/div/div/div/div/div
                            /div/ol/li[{counter}]/div/div[1]/div/h3/span/a/span""")
      counter += 1
    except NoSuchElementException:
      print("Help")
      break
  driver.back()

