from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as waiter
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located as visibility
    )
from bs4 import BeautifulSoup
import time
import pandas as pd
from pathlib import Path

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
            time.sleep(2) # Wait for page to fully load
            remove_region = self.driver.find_element(
                By.XPATH, 
                '//button[@class="Bd(0) Pb(8px) Pt(6px) Px(10px) M(0) D(ib) C($primaryColor) filterItem:h_C($primaryColor) Fz(s)" and contains(@title, "Remove")]'
                )
            remove_region.click()
        except TimeoutError: 
            print("No pre-selected region")

        add_region_button = waiter(self.driver, 10).until(
            visibility((By.XPATH, '//span[text()="Region"]/ancestor::button'))
            )
        add_region_button.click()
            
        try:
            region_select = waiter(self.driver, 10).until(
                visibility((By.XPATH, f'//span[text()="{region}"]//preceding-sibling::input'))
                )
            region_select.click()
        except TimeoutError:
            self.driver.quit()
            print("Chosen region not found among available options.")
            raise TimeoutError
        
        time.sleep(3) # Wait for Find Stocks button to be available
        find_stocks = waiter(self.driver, 10).until(
            visibility((By.XPATH, '//span[text()="Stocks"]//ancestor::button'))
            )
        find_stocks.click()

    
    def get_stocks(self, region):
        self.filter_by_region(region)

        time.sleep(5)
        html = self.driver.page_source
        self.driver.quit()

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')

        # Collecting symbol, name and price  header names
        headers = []
        header_row = table.find('tr')
        for th in header_row.find_all('th'):
            if len(headers) < 3: 
                headers.append(th.text.strip())
            else:
                break

        # Collecting table data for the 1st 3 columns (symbol, name and price)
        data = []
        rows = table.find_all('tr')[1:] # Ignoring the headers
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                data.append([cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip()])
            else:
                data.append([cols[i].text.strip() if i < len(cols) else '' for i in range(3)])

        df = pd.DataFrame(data, columns=headers)
        csv_path = Path(__file__).parent.parent.joinpath(f"stock_files\\{region}.csv")
        df.to_csv(csv_path)

