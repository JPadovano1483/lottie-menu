from requests import get
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

def get_menu(meal):
  if (meal == 'breakfast'):
    i = '1'
  elif (meal == 'lunch'):
    i = '2'
  elif (meal == 'dinner'):
    i = '3'
  else:
    return "That's not a meal you fucking idiot!"
  
  if 'i' in locals():
  # click the meal button
    driver.find_element(By.XPATH, "//tr[@class='cbo_nn_menuPrimaryRow']/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td["+i+"]/a").click()
    time.sleep(0.2)

    menu = driver.find_elements(By.XPATH, "//td[@class='cbo_nn_itemHover']")
    menu = [item.text for item in menu]
    return menu

# can probably clean this up by creating function to grab menu - lots of similar lines here
if __name__ == '__main__':
  print('Meal: ')
  meal = input()

  if (meal == 'breakfast' or meal == 'lunch' or meal == 'dinner'):
    # open link
    driver = uc.Chrome()
    driver.get("https://www.messiah.edu/NetNutrition/1")

    # click lottie button
    driver.find_element(By.XPATH, "//td[@class='cbo_nn_unitsCell']/a").click()
    time.sleep(0.1)

    # click main menu button
    driver.find_element(By.XPATH, "//div[@class='cbo_nn_unitImages']/a").click()
    time.sleep(0.1)

    print(get_menu(meal))
  else:
    print("That's not a meal you fucking idiot!")