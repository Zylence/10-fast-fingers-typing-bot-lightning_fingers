# Proof of concept to get through anti cheat validation

import pytesseract
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib import request as req

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Blocksatz-Beispiel_deutsch%2C_German_text_sample_with_fully_justified_text.svg/1024px-Blocksatz-Beispiel_deutsch%2C_German_text_sample_with_fully_justified_text.svg.png")
time.sleep(4)

img = driver.find_element(By.XPATH, '/html/body/img')
src = img.get_attribute("src")
req.urlretrieve(src, "pic.png")
time.sleep(1)

string = pytesseract.image_to_string(r'./pic.png')
words = string.split()
print(words)
