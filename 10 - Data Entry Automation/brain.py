from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

class Brain():
    def __init__(self, **kw):
        self.price: int = kw.get('p')
        self.survey_link: str = kw.get('survey')
        self.query_link = f'https://www.zillow.com/austin-tx/rentals/1-_beds/?searchQuerySt' \
       f'ate=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22A' \
       f'ustin%22%2C%22mapBounds%22%3A%7B%22west%22%3A-98.25949890039062%' \
       f'2C%22east%22%3A-97.31192809960937%2C%22south%22%3A29.95600692244' \
       f'419%2C%22north%22%3A30.630705590352363%7D%2C%22regionSelection%2' \
       f'2%3A%5B%7B%22regionId%22%3A10221%2C%22regionType%22%3A6%7D%5D%2C' \
       f'%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A' \
       f'%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%' \
       f'22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%2' \
       f'2%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%' \
       f'22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afa' \
       f'lse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%' \
       f'22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%2' \
       f'2ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A' \
       f'{self.price}%7D%2C%22price%22%3A%7B%22max%22%3A304648%7D%7D%2C%22isListVis' \
       f'ible%22%3Atrue%7D'

    def get_soup(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        website = requests.get(self.query_link, headers=headers).text
        soup = BeautifulSoup(website, 'html.parser')
        addresses = [addr.text for addr in soup.find_all(name='address', class_='list-card-addr')]
        prices = [price.text.split("/")[0] for price in soup.find_all(name='div', class_='list-card-price')]
        links = [link['href'] for link in soup.find_all(name='a', class_='list-card-link', href=True)]
        #some links don't have https:// so add it if not there
        for i in range(len(links)):
            if "https://" not in links[i]:
                links[i] = f"https://www.zillow.com/{links[i]}"
        self.results = {
            "add": addresses,
            "pr": prices,
            "links": links
        }
        self.fill_survey()

    def fill_survey(self):
        driver = '/Users/kyle/Developer/python/chromedriver'
        sel = webdriver.Chrome(driver)
        for i in range(len(self.results['links'])):
            time.sleep(2)
            sel.get(self.survey_link)
            add_inp = sel.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_inp = sel.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_inp = sel.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit = sel.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
            add_inp.send_keys(self.results['add'][i])
            price_inp.send_keys(self.results['pr'][i])
            link_inp.send_keys(self.results['links'][i])
            submit.click()

