from tqdm import tqdm
def scrape_data(driver, ads_num):
    url = driver.current_url
    links = []
    for page in tqdm(range(2, ads_num//39 + 2)):
        driver.get(url + f'&page={page}')
        for i in range(3, 43):
            try:
                link = driver.find_element_by_xpath(
                    f'//*[@id="offers_table"]/tbody/tr[{i}]/td/div/table/tbody/tr[1]/td[2]/div/h3/a').get_attribute(
                    'href')
                links.append(link.split('#')[0])
            except:
                pass
    return links