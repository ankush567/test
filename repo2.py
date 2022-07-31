import os
import time
from colorama import *
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
init()

logo = """
                      _____ _____   _____                       _     _______          _ 
                     |_   _/ ____| |  __ \                     | |   |__   __|        | |
                       | || |  __  | |__) |___ _ __   ___  _ __| |_     | | ___   ___ | |
                       | || | |_ | |  _  // _ \ '_ \ / _ \| '__| __|    | |/ _ \ / _ \| |
                      _| || |__| | | | \ \  __/ |_) | (_) | |  | |_     | | (_) | (_) | |
                     |_____\_____| |_|  \_\___| .__/ \___/|_|   \__|    |_|\___/ \___/|_|
                                              | |                                        
                                              |_|                                        
"""


def main(username, full_name, wait_):
    times_reported = 0
    while True:
        options = Options()
        options.headless = False  # Chrome Headless
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = wd.Chrome('chromedriver.exe', options=options)

        driver.get('https://help.instagram.com/contact/723586364339719')
        driver.find_element_by_xpath('//input[@name="Field258021274378282"]').send_keys(username)
        driver.find_element_by_xpath('//input[@name="Field735407019826414"]').send_keys(full_name)
        # Year
        driver.find_element_by_xpath('//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//ul[@class="_54nf"]//a[@title="2008"]').click()
        # Month
        driver.find_element_by_xpath('//a[@class="_p _55pi _5vto _55_p _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft"]//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//a[@title="February"]//span[@class="_54nh"]').click()
        # Day
        driver.find_element_by_xpath('//a[@class="_p _55pi _5vto _55_p _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft"]//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//a[@title="9"]//span[@class="_54nh"]').click()
        #
        driver.find_element_by_xpath('//select[@id="294540267362199"]//option[@value="Other"]').click()
        #
        driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()
        time.sleep(4)
        driver.close()
        times_reported += 1
        print(Fore.LIGHTBLUE_EX + f'Reported {Fore.LIGHTGREEN_EX}{times_reported}{Fore.LIGHTBLUE_EX} Time/s' + Fore.RESET)
        time.sleep(wait_)
        

def info():
    os.system('cls')
    print(Fore.LIGHTGREEN_EX + logo + Fore.RESET)
    username = input(Fore.LIGHTBLUE_EX + 'Username: @' + Fore.LIGHTGREEN_EX)
    full_name = input(Fore.LIGHTBLUE_EX + 'Full Name: ' + Fore.LIGHTGREEN_EX)
    wait_ = int(input(Fore.LIGHTBLUE_EX + 'Time to wait before the next report: ' + Fore.LIGHTGREEN_EX))
    main(username, full_name, wait_)
    

print(Fore.LIGHTGREEN_EX + logo + Fore.RESET)
info()
