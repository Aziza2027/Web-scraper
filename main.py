from selenium import webdriver
from price import Pricer
import pandas as pd
from scraper import scrape_data
from paths import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
driver.get('https://www.olx.uz/nedvizhimost/kvartiry/prodazha/')

x_paths = {
    'start_path': ['//*[@id="param_price"]/div[2]/div[1]/a', '//*[@id="param_price"]/div[2]/div[1]/label/input'],
    'end_path': ['//*[@id="param_price"]/div[2]/div[2]/a', '//*[@id="param_price"]/div[2]/div[2]/label/input'],
    'enter_key_path': '//*[@id="param_price"]/div[2]/div[2]/label/input',
    'ads_path': '//*[@id="offers_table"]/tbody/tr[1]/td/div[1]/p'
}
links = []
pricer = Pricer(driver, x_paths)
while pricer.end_price < pricer.price_limit:
    ads_num = pricer.set_prices()
    links.extend(scrape_data(driver, ads_num))

list = pd.DataFrame(list(set(links)))
print(list.shape)
list.to_csv('l.csv')