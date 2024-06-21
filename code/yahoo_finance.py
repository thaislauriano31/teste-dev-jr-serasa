from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as waiter
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located as visibility
    )
from bs4 import BeautifulSoup
import time
import pandas as pd

class YahooFinance():
    def __init__(self, url):
        self.url = url
        self.driver = self.get_driver()

    def get_driver(self) -> webdriver:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.url)
        return driver

    def filter_by_region(self, region):
        # Removing any pre-selected region
        try:
            time.sleep(2)
            remove_region = waiter(self.driver, 20).until(visibility((By.XPATH, '//button[@class="Bd(0) Pb(8px) Pt(6px) Px(10px) M(0) D(ib) C($primaryColor) filterItem:h_C($primaryColor) Fz(s)" and contains(@title, "Remove")]')))
            remove_region.click()
        except: 
            print("No pre-selected region")

        try:
            region_button = waiter(self.driver, 10).until(visibility((By.XPATH, '//span[text()="Region"]/ancestor::button')))
            region_button.click()

            region_select = waiter(self.driver, 10).until(visibility((By.XPATH, f'//span[text()="{region}"]//preceding-sibling::input')))
            region_select.click()
        except:
            print("Chosen region not found among available options.")
            return
        
        time.sleep(3)
        find_stocks = waiter(self.driver, 10).until(visibility((By.XPATH, '//span[text()="Stocks"]//ancestor::button')))
        find_stocks.click()

    
    def get_stocks(self, region):
        self.filter_by_region(region)

        time.sleep(5)
        html = self.driver.page_source
        self.driver.quit()

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')

        headers = []
        header_row = table.find('tr')
        for th in header_row.find_all('th'):
            if len(headers) < 3: 
                headers.append(th.text.strip())
            else:
                break

        data = []
        rows = table.find_all('tr')[1:] # Ignoring the headers
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                data.append([cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip()])
            else:
                data.append([cols[i].text.strip() if i < len(cols) else '' for i in range(3)])

        df = pd.DataFrame(data, columns=headers)
        df.to_csv(f"stock_files\\{region}.csv")

