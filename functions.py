from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decorators import make_line_less_70


@make_line_less_70
def write_to_file(file_name, text):
  with open(f"AWS_{file_name}.txt", 'a') as file:
    file.write(text + '\n')


def get_text(driver, counter):
  try:
    element = driver.find_elements(by=By.XPATH, value=f"""/html/body/div[2]/div/div/div[2]/main/div[3]/div/div[4]/div[1]/div/div/div/div[2]/div/div/div/div/div[4]/div[1]/p[{counter}]""")
    if len(element) == 0:
      element = driver.find_elements(by=By.XPATH, value=f"""/html/body/div[2]/div/div/div[2]/main/div[2]/div[1]/div[1]/div/div/div[4]/div[1]/p[{counter}]""")
  except NoSuchElementException:
    return None
  if element:
    return element[0].text
  else:
    return


def get_element(driver, aws_service_element):
  service_name = str(aws_service_element.text)
  aws_service_element.click()
  try:
    element = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.XPATH, f"""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]/div/section[1]/div/div/div/div/div/div/ol/li[1]/div/div[1]/div/h3/span/a/span"""))
      )
  except NoSuchElementException:
    element = WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.XPATH, f"""/html/body/div[2]/div/div/div[2]/main/div[1]/div/div[1]/div[4]/div/section[1]/div[2]/div/div/div/div/div/ol/li[1]/div/div[1]/div/h3/span/a/span"""))
      )
  element_counter = 2
  text = "foo"
  while element:
    try:
      element.click()
      text_counter = 1
      while text:
        text = get_text(driver, text_counter)
        write_to_file(service_name, str(text))
        text_counter += 1
      driver.back()
      driver.implicitly_wait(1)
      element = driver.find_element(by=By.XPATH, 
                            value=f"""/html/body/div[2]/div/div/div[2]/main/div[1]
                            /div/div[1]/div[4]/div/section[1]/div/div/div/div/div
                            /div/ol/li[{element_counter}]/div/div[1]/div/h3/span/a/span""")
      element_counter += 1
    except NoSuchElementException:
      print("Help")
      break
  driver.back()

