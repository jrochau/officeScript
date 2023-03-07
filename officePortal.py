import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")

chrome_driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s --incognito"

driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

driver.get('https://portal.office.com/')
#driver.quit()

while True:
    if driver.window_handles:
        try:
            driver.switch_to.window(driver.window_handles[0])
        except:
            break
driver.quit()
