from requests import get
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

def get_menu():
  return driver.find_elements(By.XPATH, "//td[@class='cbo_nn_itemHover']")

if __name__ == '__main__':
  print('Meal: ')
  meal = input()

  # open link
  driver = uc.Chrome()
  driver.get("https://www.messiah.edu/NetNutrition/1")

  # click lottie button
  driver.find_element(By.XPATH, "//td[@class='cbo_nn_unitsCell']/a").click()
  time.sleep(0.1)

  # click main menu button
  driver.find_element(By.XPATH, "//div[@class='cbo_nn_unitImages']/a").click()
  time.sleep(0.1)

  if (meal == 'breakfast'):
    # click breakfast button
    driver.find_element(By.XPATH, "//tr[@class='cbo_nn_menuPrimaryRow']/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").click()
    time.sleep(0.2)

    # get breakfast menu
    breakfastMenu = get_menu()
    breakfastMenu = [item.text for item in breakfastMenu]
    print(breakfastMenu)

  elif (meal == 'lunch'): 
    # click lunch button
    driver.find_element(By.XPATH, "//tr[@class='cbo_nn_menuPrimaryRow']/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()
    time.sleep(0.2)

    # get lunch menu
    lunchMenu = get_menu()
    lunchMenu = [item.text for item in lunchMenu]
    print(lunchMenu)

  elif (meal == 'dinner'):
    # click dinner button
    driver.find_element(By.XPATH, "//tr[@class='cbo_nn_menuPrimaryRow']/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a").click()
    time.sleep(0.2)

    # get dinner menu
    dinnerMenu = get_menu()
    dinnerMenu = [item.text for item in dinnerMenu]
    print(dinnerMenu)

  else:
    print("That's not a meal you fucking idiot!")



