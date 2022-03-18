from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_drive_path = "C:\\Users\\Pichau\\Desktop\\JAVASCRIPT\\chromedriver"
ZILLOWS_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.87346877050781%2C%22east%22%3A-121.99318922949219%2C%22south%22%3A37.338736052181154%2C%22north%22%3A38.209284185107144%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
DOCS_URL = "https://forms.gle/UNNHizn2KYmF13Hv6"

#get the infos
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get(ZILLOWS_URL)
driver.maximize_window()
time.sleep(5)
elems_links = driver.find_elements(By.CSS_SELECTOR,"div.list-card-top a")
all_links = [elem.get_attribute('href') for elem in elems_links]
print(all_links)
elems_prices = driver.find_elements(By.CSS_SELECTOR,"div.list-card-info div.list-card-heading div")
all_prices = [price.text for price in elems_prices]
print(all_prices)
elems_adress = driver.find_elements(By.CSS_SELECTOR,"div.list-card-info a address")
all_adress = [adress.text for adress in elems_adress]
print(all_adress)
time.sleep(5)

#filling the form
for i in range(len(elems_adress)):
    driver.get(DOCS_URL)
    driver.maximize_window()
    time.sleep(5)
    adress_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    adress_input.send_keys(f"{all_adress[i]}")
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(f"{all_prices[i]}")
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(f"{all_links[i]}")
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()