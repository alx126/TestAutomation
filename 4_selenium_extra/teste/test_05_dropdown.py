import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

"""
########### Dropdown-uri in Selenium

Pentru a putea intercationa mai usor cu elemente de tip dropdown, libraria Select vine in ajutorul nostru

Pasi pentru a selecta o optiune pe un dropdown:
1. Declaram o variabila de tip WebElement care reprezinta dropdown-ul cu tag-ul HTML <select>
2. Declaram o variabila de tip Select care primeste ca argument elementul declarat la punctul 1
3. Selectam optiuniea dorita dupa text, valoare, index, etc.


"""


class TestDropdown(unittest.TestCase):
    DROPDOWN = (By.ID, "dropdown")

    def setUp(self) -> None:
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
        self.driver.implicitly_wait(1)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_select_by_text(self):
        dropdown = self.driver.find_element(*self.DROPDOWN)
        select = Select(dropdown)

        text_optiune_de_selectat = "Option 1"

        select.select_by_visible_text(text_optiune_de_selectat)
        time.sleep(1)

        text_optiune_selectata = select.first_selected_option.text

        assert text_optiune_selectata == text_optiune_de_selectat

    def test_select_by_value(self):
        dropdown = self.driver.find_element(*self.DROPDOWN)
        select = Select(dropdown)

        text_value_de_selectat = "2"

        select.select_by_value(text_value_de_selectat)
        time.sleep(1)

        text_value_selectat = select.first_selected_option.get_attribute("value")

        assert text_value_selectat == text_value_de_selectat

    def test_select_by_index(self):
        dropdown = self.driver.find_element(*self.DROPDOWN)
        select = Select(dropdown)

        index_de_selectat = "1"

        select.select_by_index(index_de_selectat)
        time.sleep(1)

        text_optiune_selectata = select.first_selected_option.text

        assert text_optiune_selectata == "Option 1"