from p6_pom_bdd.pages.base_page import BasePage


class HomePage(BasePage):

    def navigate_to_home_page(self):
        self.driver.get(self.BASE_URL)