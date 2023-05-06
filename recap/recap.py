import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Search(TestCase):
    driver = None
    LINK = "https://demo.nopcommerce.com/"
    SEARCH_INPUT = (By.ID, "small-searchterms")
    DROPDOWN_SORT = (By.ID, "products-orderby")
    SEARCH_BUTTON = (By.XPATH, '//button[text()="Search"]')
    PRODUCT_TITLES = (By.XPATH, '//h2[@class="product-title"]')
    PRODUCT_SUGGERSTIONS = (By.XPATH, "//div[@class='search-box store-search-box']//span")
    LOADING_ANIMATION = (By.XPATH, "//div[@class='ajax-products-busy']")
    PRODUCT_PRICES = (By.XPATH, "//div[@class='prices']")

    # definim metoda setUp
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(2)
        # self.driver.implicitly_wait(2)

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(expected_conditions.presence_of_element_located(element_locator))

    # definim metoda tearDown
    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        cuvant_cautat = "Laptop"

        self.driver.find_element(*self.SEARCH_INPUT).send_keys(cuvant_cautat)

        # linia de mai sus e echivalent cu urmatoarele linii:
        # search_input =  self.driver.find_element(*self.SEARCH_INPUT)
        # search_input.send_keys(cuvant_cautat)

        self.driver.find_element(*self.SEARCH_BUTTON).click()

        self.wait_for_element_to_be_present(self.PRODUCT_TITLES, 3)

        lista_rezultate = self.driver.find_elements(*self.PRODUCT_TITLES)

        for rezultat in lista_rezultate:
            print(f">>>{rezultat.text}")
            assert cuvant_cautat.lower() in rezultat.text.lower()

    def test_search_suggestions(self):
        cuvant_cautat = "Laptop"
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(cuvant_cautat)
        self.wait_for_element_to_be_present(self.PRODUCT_SUGGERSTIONS, 3)

        lista_sugestii = self.driver.find_elements(*self.PRODUCT_SUGGERSTIONS)

        for suggestion in lista_sugestii:
            assert cuvant_cautat in suggestion.text

    def test_sort_price_low_to_high(self):
        cuvant_cautat = "Laptop"
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(cuvant_cautat)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        self.wait_for_element_to_be_present(self.PRODUCT_TITLES, 3)

        dropdown = self.driver.find_element(*self.DROPDOWN_SORT)
        select = Select(dropdown)
        select.select_by_visible_text("Price: Low to High")

        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.text_to_be_present_in_element_attribute(self.LOADING_ANIMATION, "style", "none"))

        price_element_list = self.driver.find_elements(*self.PRODUCT_PRICES)

        price_float_list = list()

        for price in price_element_list:
            price_value = price.text[1::1].replace(",", "")
            price_float_list.append(float(price_value))

        print(f"Lista initiala: {price_float_list}")

        price_list_sorted = list()

        price_list_sorted.extend(price_float_list)

        price_list_sorted.sort()

        print(price_list_sorted)
        print(price_float_list)
        assert price_list_sorted == price_float_list

