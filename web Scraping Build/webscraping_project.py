# here we will scape data and keep in a seperate Folder...
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from pathlib import Path

import os

datafolderDir = 'data'
rawfolderDir = 'raw'

BASE_DIR = Path(__file__).resolve().parent.parent #raw folder is inside the data so - parent.parent
RAW_DATA_DIR = BASE_DIR.joinpath(datafolderDir).joinpath(rawfolderDir)


# Ensure the directory exists
os.makedirs(RAW_DATA_DIR, exist_ok=True) #check weather the Folder Exist

driver = webdriver.Chrome()
query = "Laptop"
#creating afile to store data 
#file variable
file = 0
try:
    for i in range(1, 20):
        #here get() to put URL of a website
        driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

        #By.ClASS_NAME - It is a Locator
        elems = driver.find_elements(By.CLASS_NAME, 'tUxRFH')
    
        print(f'{len(elems)} items found') #tell the no of Items Found

        for e in elems:
            d = e.get_attribute("outerHTML") #outerHTML
            file_path = os.path.join(RAW_DATA_DIR, f'{query}_{file}.html') #here we are looking for the file inside the Dir with paericular name
            with open(file_path, "w", encoding = "utf-8") as f:
                f.write(d)
            file += 1
        
        print(f'Data saved in : {RAW_DATA_DIR}') 

    time.sleep(2) #Sleep for 2 sec

finally:
    driver.close() #Close the driver after work
