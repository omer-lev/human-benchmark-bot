from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import uuid


PATH = "PATH TO YOUR CHROME DRIVER"
driver = webdriver.Chrome(PATH)

driver.get("https://humanbenchmark.com/tests/reactiontime")


while True:
    for num in range(5):

        if num == 0:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "view-splash"))).click()
            
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "view-go"))).click()

        if num < 4:
            score = (driver.find_element_by_css_selector("h1 div").get_attribute("innerHTML")).replace("ms", "")

            if int(score) < 20:
                driver.save_screenshot("C:\humanbenchmark\{} -- {}.png".format(score, uuid.uuid4()))

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "view-result"))).click()
        
        elif num == 4:
            score = (driver.find_element_by_css_selector("h1").get_attribute("innerHTML")).replace("ms", "")

            if int(score) < 20:
                driver.save_screenshot("C:\humanbenchmark\{} -- {}.png".format(score, uuid.uuid4()))
            
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "secondary"))).click()
            num = 0