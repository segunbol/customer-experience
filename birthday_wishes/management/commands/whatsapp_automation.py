import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from birthday_wishes.models import Customer
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        data_list = []
        customers = Customer.objects.all()
        dated = datetime.now().strftime('%m-%d')
        for customer in customers:
            if customer.date_of_birth.strftime("%m-%d") == dated:
                data_list.append(customer)
            else:
                pass
        print(data_list)
        s = Service(r"C:\Users\EMMANUEL\chromedriver")
        browser = webdriver.Chrome(service=s)
        browser.get("https://web.whatsapp.com")
        """browser = webdriver.Edge(service=s)
        browser.get("https://web.whatsapp.com")"""
        slack = input("")
        count = 0
        not_count = 0
        retry1 = 0
        for peeps in data_list:
            while True:
                try:
                    browser.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').clear()
                    print("First one worked")
                    browser.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(peeps.name) # search bar
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    print("First didn't work")
                time.sleep(3)
                retry = 0
                try:
                    browser.find_element(By.XPATH, '//span[@title = "{}"]'.format(peeps)).click()  # click contact
                    if retry < 1:
                        print(f"{peeps} is on whatsapp")
                        count = count + 1
                    else:
                        print(f'{peeps} might have been sent')
                    """the assert method should come in here, if it is false, use the Keys.Return function"""
                    n = 0
                    retry = retry + 1
                    time.sleep(2)
                    # browser.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]').clear()
                    g = 0
                    try:
                        '''browser.find_element(By.XPATH, '//span[@title = "{}"]'.format(peeps)).click()
                        time.sleep(1)'''
                        '''browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
                                            ).clear()'''
                        '''//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]
                        //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'''
                        browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'
                                            ).send_keys(f"Happy Birthday {peeps.name}, Rosabon Financial Services wants to sieze this opportunity to show our appreciation for your patronage and wish you long life and properity. Kindly visit this link for a virtual celebration")  # the message bar
                        time.sleep(1)
                        g = g + 1
                        browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div['
                                                    '2]/button/span').click()  # the send button
                        break
                    except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                        print('message bar was not clicked')
                        try: 
                            browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p' ).send_keys(f"Happy Birthday {peeps.name}, Rosabon FS wants to sieze this opportunity to show our appreciation for your patronage and wish you long life and properity. Kindly visit this link for a virtual celebration")
                            print('message bar was clicked using class name')  # the message bar
                            browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div['
                                                        '2]/button/span').click()  # the send button
                            break
                        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                            print("message bar was not clicked using class name")
                    if g < 5:
                        continue
                except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
                    print(f"{peeps} is not on whatsapp")
                    not_count = not_count + 1
                    break
        print(f"A total of {count} were sent and a total of {not_count} is not on whatsapp")

        sun = input("Press enter to quit")
        browser.quit()

"""
//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span
'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
"""