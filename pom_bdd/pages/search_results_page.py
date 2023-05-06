from selenium.webdriver.common.by import By

from pom_bdd.pages.base_page import BasePage


class SearchResultsPage(BasePage):

    PRODUCT_ITEM = (By.CLASS_NAME, "product-item")
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")

    def are_all_products_displayed(self):
        self.wait_for_element_to_be_present(self.PRODUCT_ITEM, 3)
        product_item_list = self.find_all(self.PRODUCT_ITEM)

        for item in product_item_list:
            if not item.is_displayed():
                return False

        return True

    def are_all_titles_containing_text(self, text: str):
        titles_list = self.find_all(self.PRODUCT_TITLE)

        for title in titles_list:
            if text.lower() not in title.text.lower():
                return False

        return True