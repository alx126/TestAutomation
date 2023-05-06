from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseSite:

    LOGGED_USER_BUTTON = (By.CSS_SELECTOR, 'span#textLoginName')

    FRAME_NEW_ENTITY = (By.XPATH, '//*[@id="RadWindowWrapper_POPUP_FIRST_WINDOW"]/table/tbody/tr[2]/td[2]/iframe')

    DIV_CONFIRM_ACTION = (By.XPATH, '//*[@id="RadWindowWrapper_confirm1681147905224"]')
    CONFIRM_ACTION__OK_BUTTON_LIST = (By.CSS_SELECTOR, 'div[id*=confirm] > div > div:nth-child(2) > a:nth-child(1)')
    CONFIRM_ACTION__CANCEL_BUTTON_LIST = (By.CSS_SELECTOR, 'div[id*=confirm] > div > div:nth-child(2) > a:nth-child(2)')

    GRID_LV = (By.CSS_SELECTOR, '#ctl00_MCPH_ListView_gridView')
    GRID_LV_FILTER_BUTTON = (
    By.XPATH, '//*[@id="ctl00_MCPH_ListView_gridView_ctl00_ctl02_ctl00_RadGridHeaderMenu"]/ul/li[1]/a/span')
    #GRID_LV_FILTER_NUMBER = (By.XPATH, '//*[@id="ctl00_MCPH_ListView_gridView_ctl00_ctl02_ctl03_FilterTextBox_NUMBER"]')
    #GRID_LV_1st_CELL = (By.CSS_SELECTOR, '#ctl00_MCPH_ListView_gridView_ctl00__0')


    def __init__(self, driver: webdriver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.find(locator).click()

    def context_click(self, locator):
        ActionChains(self.driver).context_click(self.find(locator)).perform()

    def write(self, locator, text):
        self.find(locator).send_keys(text)

    def select_and_overwrite(self, locator, text):
        field = self.find(locator)
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(text)

    def get_element_text(self, locator):
        return self.find(locator).text

    def get_element_attribute_value(self, locator):
        return self.find(locator).get_attribute("value")

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def wait_is_visible(self, seconds, locator):
        wait = WebDriverWait(self.driver, seconds)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

    def wait_switch_to_frame(self, seconds_to_wait, frame_locator):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

    def switch_to_default(self):
        self.driver.switch_to.default_content()
        self.driver.implicitly_wait(2)

    def select_stack_menu(self, menu_locator):
        self.click(menu_locator)

    def refresh_menu(self, refresh_locator):
        self.click(refresh_locator)

    def confirm_action_click_ok(self):
        confirm_button_ok_list = self.driver.find_elements(*self.CONFIRM_ACTION__OK_BUTTON_LIST)
        for button in confirm_button_ok_list:
            if button.is_displayed():
                button.click()

    def confirm_action_click_cancel(self):
        confirm_button_cancel_list = self.driver.find_elements(*self.CONFIRM_ACTION__CANCEL_BUTTON_LIST)
        for button in confirm_button_cancel_list:
            if button.is_displayed():
                button.click()