import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
class Parser:
    def __init__(self, driver):
        self.driver = driver
    def parser_name(self,articul):
        url = f'https://www.wildberries.ru/catalog/{articul}/detail.aspx'
        self.driver.get(url=url)
        time.sleep(2)
        name = (self.driver.find_element(By.XPATH, "//h1[@class='product-page__title']").text)
        return(name)

    def parser_price(self,articul):
        url = f'https://www.wildberries.ru/catalog/{articul}/detail.aspx'
        self.driver.get(url=url)
        time.sleep(2)
        price_script = "return document.querySelector('ins.price-block__final-price.wallet').innerText;"
        price = self.driver.execute_script(price_script).replace(u'\xa0', ' ')
        return(price)

    def parser_rating(self,articul):
        url = f'https://www.wildberries.ru/catalog/{articul}/detail.aspx'
        self.driver.get(url=url)
        time.sleep(2)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        rating = soup.find('span', class_='product-review__rating address-rate-mini address-rate-mini--sm').text
        return(rating)

    def parser_count_evaluation(self,articul):
        url = f'https://www.wildberries.ru/catalog/{articul}/detail.aspx'
        self.driver.get(url=url)
        time.sleep(2)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        rating = soup.find('span', class_='product-review__count-review j-wba-card-item-show j-wba-card-item-observe').text
        rating = rating[:-7]
        return (rating)
