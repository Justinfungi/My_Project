from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

def get_driver():
    chrome_options = Options()
    chrome_options.headless=False
    executable= "/home/fish/Documents/WebScraping/driver/chromedriver_ubuntu"
    driver = webdriver.Chrome(executable_path=executable, options=chrome_options)
    return driver

def login_in(driver):
    username= WebDriverWait(driver, 10)          .until(EC.element_to_be_clickable
                     ((By.CSS_SELECTOR, "input[name='loginfmt']"))
                    )

    username.clear()
    username.send_keys("fung0311@connect.hku.hk")

    button = WebDriverWait(driver, 2)         .until(EC.element_to_be_clickable
                    ((By.CSS_SELECTOR, "input[type='submit']"))
                   ).click()

    time.sleep(4)

    username= WebDriverWait(driver, 10)          .until(EC.element_to_be_clickable
                     ((By.CSS_SELECTOR, "input[name='Password']"))
                    )

    username.clear()
    username.send_keys("fhj03137120128811")
    button = WebDriverWait(driver, 2)         .until(EC.element_to_be_clickable
                    ((By.CSS_SELECTOR, "span[class='submit']"))
                   ).click()


    button = WebDriverWait(driver, 2)         .until(EC.element_to_be_clickable
                    ((By.CSS_SELECTOR, "input[id='idSIButton9']"))
                   ).click()
    return

def Share_list(share_list_names,driver):
    Share_List = driver.find_elements("xpath","//button[@role='link']")
    for i in Share_List:
        share_list_names.append(i.text)
    print(share_list_names)
    return

def local():
    entries = os.listdir('/home/fish/Share/')
    print(entries)
    return entries

def main():
    share_list_names=[]
    local_list=local()

    url="https://connecthkuhk-my.sharepoint.com/personal/fung0311_connect_hku_hk/_layouts/15/onedrive.aspx?isAscending=false&id=%2Fpersonal%2Ffung0311%5Fconnect%5Fhku%5Fhk%2FDocuments%2FShare&sortField=Modified"
    driver=get_driver()
    driver.get(url)

    login_in(driver)

    Share_list(share_list_names,driver)


    '''
    button = WebDriverWait(driver, 2)         .until(EC.element_to_be_clickable
                    ((By.CSS_SELECTOR, "button[name='Upload']"))
                   ).click()
    button = WebDriverWait(driver, 2)         .until(EC.element_to_be_clickable
                    ((By.CSS_SELECTOR, "button[name='Files']"))
                   ).click()

    for i in entries:
        if i not in share_list_names:
            button = WebDriverWait(driver, 2)         .until(EC.element_to_be_clickable
                            ((By.CSS_SELECTOR, "button[name='Upload']"))
                           ).click()
            button = WebDriverWait(driver, 2)         .until(EC.element_to_be_clickable
                            ((By.CSS_SELECTOR, "button[name='Files']"))
                           ).click()
    '''
    return 0


main()
