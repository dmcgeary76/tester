from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.bestbuy.com/site/refrigerators/french-door-refrigerators/abcat0901004.c?id=abcat0901004'

'''
def find_page_items(driver,link):
    driver.get(link)
    items = [item.find_element_by_tag_name('class').get_attribute('sku-title')]
    for item in items:
        res = requests.get(item,headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(res.text,"lxml")
        name = soup.select_one("h1[itemprop='name']").text.strip()
        print(name)
'''

def get_appliances(driver, link):
    driver.get(link)
    res = requests.get(link, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "lxml")
    print(soup)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
        get_appliances(driver,url)
    finally:
        driver.quit()
