import time
from selenium.webdriver.common.keys import Keys

class Pricer:
    def __init__(self, driver, x_paths):
        self.driver = driver
        self.start_price = 0
        self.end_price = 0
        self.start_path = x_paths['start_path']
        self.end_path = x_paths['end_path']
        self.enter_path = x_paths['enter_key_path']
        self.ads_path = x_paths['ads_path']
        self.price_limit = 4 * 10**9

    def determine_ads_number(self):
        self.driver.find_element_by_xpath(self.start_path[0]).click()
        for _ in range(len(str(self.start_price))+1):
            self.driver.find_element_by_xpath(self.start_path[1]).send_keys(Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.start_path[1]).send_keys(self.start_price)

        self.driver.find_element_by_xpath(self.end_path[0]).click()
        for _ in range(len(str(self.end_price))+1):
            self.driver.find_element_by_xpath(self.end_path[1]).send_keys(Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.end_path[1]).send_keys(self.end_price)

        self.driver.find_element_by_xpath(self.enter_path).send_keys(Keys.ENTER)

        time.sleep(3)
        num_ads = self.driver.find_element_by_xpath(self.ads_path).text
        try:
            num_ads = int(''.join(num_ads.split()[2:]))
        except:
            print(num_ads)
            raise AttributeError
        print(num_ads, self.start_price, self.end_price)
        return num_ads

    def increase(self):
        print('Increasing price...')
        self.end_price += 4 * 10**6
        return self.determine_ads_number()

    def decrease(self):
        print('Decreasing price...')
        self.end_price -= 5 * 10**5
        return self.determine_ads_number()

    def set_prices(self):
        self.start_price = self.end_price
        ads_num = self.increase()

        while ads_num < 975:
            ads_num = self.increase()
        while ads_num > 975:
            ads_num = self.decrease()

        return ads_num