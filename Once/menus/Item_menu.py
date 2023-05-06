import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains, Keys

from Once.sites.webdev import WebDev
from Once.pages.login_page_webdev import LoginPageWebDev


class ItemMenu(WebDev):
    # LOGGED_USER_BUTTON = (By.CSS_SELECTOR, 'span#textLoginName')

    ITEM_STACK_MENU = (By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[4]')

    REFRESH_MENU_BUTTON = (By.CSS_SELECTOR, 'span#rpText.rpText')
    EXPAND_ITEM_BUTTON = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/div/span[2]')

    ITEM_INS_FOLDER = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li[9]/div/span[3]')
    ITEMS_FOLDER = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/div/span[3]')

    ITEMS_INS_CM__NEW = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[1]/a/span')

    ITEM_CM__NEW = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[1]')
    ITEM_CM__COPY_NEW = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[2]')
    ITEM_CM__EDIT = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[3]')
    ITEM_CM__EDIT_IN_GRID = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[4]')
    ITEM_CM__LINK_FILE = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[5]')
    ITEM_CM__LINK_DOC = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[6]')
    ITEM_CM__ADD_ITEM_TYPES = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[7]')
    ITEM_CM__REM_ITEM_TYPES = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[8]')
    ITEM_CM__NEW_BOM_LINE = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[9]')
    ITEM_CM__COPY_DATA_FROM = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[10]')

    ADD_ITEM_DIALOG__ITEM_NUMBER = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_NUMBER_rdTextBox"]')
    ADD_ITEM_DIALOG__ITEM_TITLE = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_ITEM_TITLE_rdTextBox"]')
    ADD_ITEM_DIALOG__ITEM_DESC = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_ITEM_DESC_rdTextBox"]')
    ADD_ITEM_DIALOG__SAVE_AND_CLOSE_BUTTON = (By.XPATH, '//*[@id="DVTopMenu"]/li[2]/span/span')

    UPLOAD_FILES_DIALOG__TAB_EXISTING = (By.XPATH, '//*[@id="tabstrip-tab-1"]')  # //*[@id="tabstrip-tab-1"] //*[@id="tabstrip-tab-1"]/span[2]
    UPLOAD_FILES_DIALOG__TAB_FROM_DISK = (By.XPATH, '//*[@id="tab2"]')
    UPLOAD_FILES_DIALOG__TAB_HELP = (By.XPATH, '//*[@id="tab4"]')
    UPLOAD_FILES_DIALOG__BUTTON_CHOOSE_FILES = (By.XPATH, '//*[@id="chooseFiles"]')
    UPLOAD_FILES_DIALOG__BUTTON_SAVE = (By.XPATH, '//*[@id="btnSave"]')
    UPLOAD_FILES_DIALOG__BUTTON_CLOSE = (By.XPATH, '//*[@id="btnSave"]')
    UPLOAD_FILES_DIALOG__EXISTING__GRID_LV_1_CELL = (By.XPATH,
                                                     '/html/body/div[1]/div[2]/div[1]/div/div[3]/table/tbody/tr['
                                                     '1]/td[1]')
    UPLOAD_FILES_DIALOG__EXISTING__FILES_LIST = (By.XPATH, '//div[@id="MCPH_DetailView_detailViewLeftPane"]/div/div/div'
                                                           '/div[@id="kendoParentGrid"]/div/div/table/tbody['
                                                           '@role="rowgroup"]/tr')

    FRAME_ADD_ITEM = (By.XPATH, '//*[@id="RadWindowWrapper_POPUP_FIRST_WINDOW"]/table/tbody/tr[2]/td[2]/iframe')
    FRAME_UPLOAD_FILES = (By.XPATH, '//*[@id="RadWindowWrapper_GENERIC_SEARCH_WINDOW"]/table/tbody/tr[2]/td[2]/iframe')

    GRID_LV = (By.CSS_SELECTOR, '#ctl00_MCPH_ListView_gridView')
    GRID_LV_FILTER_BUTTON = (By.XPATH, '//*[@id="ctl00_MCPH_ListView_gridView_ctl00_ctl02_ctl00_RadGridHeaderMenu'
                                       '"]/ul/li[1]/a/span')

    GRID_LV_FILTER_NUMBER = (By.XPATH, '//*[@id="ctl00_MCPH_ListView_gridView_ctl00_ctl02_ctl03_FilterTextBox_NUMBER"]')
    GRID_LV_1st_CELL = (By.CSS_SELECTOR, '#ctl00_MCPH_ListView_gridView_ctl00__0')
    GRID_LV_NO_RECORDS = (By.CSS_SELECTOR, 'tr.rgNoRecords')

    ITEM_DV__ITEM_NUMBER = (By.CSS_SELECTOR, '#MCPH_DetailView_uiWeb_NUMBER_rdTextBox')
    ITEM_DV__BUTTON_DELETE = (By.XPATH, '//*[@id="DVTopMenu"]/li[4]/span/span')
    ITEM_DV__TAB_FILE = (By.XPATH, '//*[@id="tabDetailView"]/div/ul/li[5]/a')

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    #
    #
    # def click(self, locator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     self.driver.find_element(*locator).click()
    #
    # def context_click(self, locator):
    #     ActionChains(self.driver).context_click(self.driver.find_element(*locator)).perform()
    #
    # def write(self, locator, text):
    #     self.driver.find_element(*locator).send_keys(text)
    #
    # def select_and_overwrite(self, locator, text):
    #     field = self.driver.find_element(*locator)
    #     field.send_keys(Keys.CONTROL, "a")
    #     field.send_keys(Keys.BACKSPACE)
    #     field.send_keys(text)
    #
    # def get_element_text(self, locator):
    #     return self.driver.find_element(*locator).text
    #
    # def get_element_attribute_value(self, locator):
    #     return self.driver.find_element(*locator).get_attribute("value")
    #
    # def wait_is_visible(self, seconds, locator):
    #     WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(locator))
    #
    # def wait_switch_to_frame(self, seconds, locator):
    #     WebDriverWait(self.driver, seconds).until(EC.frame_to_be_available_and_switch_to_it(locator))
    #
    # def switch_to_default(self):
    #     self.driver.switch_to.default_content()
    #     self.driver.implicitly_wait(2)
    #
    # def select_stack_menu(self, menu_locator):
    #     # self.driver.find_element(*menu_locator).click()
    #     self.click(menu_locator)
    #
    # def refresh_menu(self):
    #     self.click(self.REFRESH_MENU_BUTTON)

    # def sign_in_admin(self):
    #     self.driver.find_element(self.EMAIL_INPUT).send_keys(
    #         'admin@engsys360dev.onmicrosoft.com')
    #     time.sleep(1)
    #     self.driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('Es2K-Es2K')
    #     time.sleep(1)
    #     self.click((By.CSS_SELECTOR, 'button#next'))
    #     time.sleep(1)
    #     self.driver.implicitly_wait(2)

    # def sign_in_Engsys(self):
    #     self.driver.find_element(By.CSS_SELECTOR, 'input#logonIdentifier').send_keys(
    #         'admin@engsys360dev.onmicrosoft.com')
    #     time.sleep(1)
    #     self.driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('Es2K-Es2K')
    #     time.sleep(1)
    #     self.click((By.CSS_SELECTOR, 'button#EngSys'))
    #     time.sleep(1)
    #     self.driver.implicitly_wait(2)
    #
    # def test_sign_in_admin(self):
    #     self.sign_in_admin()
    #     user = 'Admin'
    #     self.wait_is_visible(5, self.LOGGED_USER_BUTTON)
    #     logged_user = self.driver.find_element(*self.LOGGED_USER_BUTTON).text
    #     self.assertEqual(logged_user, user, 'Different user logged in.')
    #
    # def test_sign_in_EngSys(self):
    #     self.sign_in_Engsys()

    # def test_select_menu_Project(self):
    #     self.sign_in_admin()
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[1]').click()
    #     time.sleep(1)

    # def test_iterate_through_menus(self):
    #     self.sign_in_admin()
    #     menus_list = self.driver.find_elements(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li')
    #     # for menu in menus_list:
    #     #     menu.click()
    #     #     self.driver.implicitly_wait(2)
    #     #     self.driver.back()
    #     #     self.driver.implicitly_wait(2)
    #     #     time.sleep(1)
    #
    #     for i in range(1, len(menus_list)):
    #         self.click((By.XPATH, f'//*[@id="BarMenu"]/ul/descendant::li[{i}]'))
    #         self.driver.implicitly_wait(2)
    #         time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[1]').click()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[2]').click()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[3]').click()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[4]').click()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[5]').click()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[6]').click()
    #     self.driver.implicitly_wait(2)
    #     # time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[7]').click()
    #     self.driver.implicitly_wait(2)
    #     # time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[8]').click()
    #     self.driver.implicitly_wait(2)
    #     # time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[9]').click()
    #     self.driver.implicitly_wait(2)
    #     # time.sleep(1)
    #     self.driver.back()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     product_menu = self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/li[2]/a/span/span[2]').text
    #     # //*[@id="BarMenu"]/ul/li[2]/a/span/span[2]/text()
    #
    # def test_document_menu_iterate_folders(self):
    #     self.sign_in_admin()
    #     self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/li[3]/a/span/span[2]').click()
    #     self.driver.implicitly_wait(2)
    #
    #     self.driver.find_element(By.CSS_SELECTOR, 'span#rpText.rpText').click()
    #     self.driver.implicitly_wait(2)
    #
    #     self.driver.find_element((By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[1]'))
    #     self.driver.implicitly_wait(2)
    #
    #     self.driver.find_element((By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]'))
    #     self.driver.implicitly_wait(2)
    #
    # def test_create_new_item_instrument(self):
    #     self.sign_in_admin()
    #     self.select_stack_menu(self.ITEM_STACK_MENU)
    #     self.driver.implicitly_wait(2)
    #     #time.sleep(1)
    #     self.refresh_menu()
    #     self.driver.implicitly_wait(2)
    #     #time.sleep(1)
    #     self.click(self.EXPAND_ITEM_BUTTON)
    #     self.driver.implicitly_wait(2)
    #     #time.sleep(1)
    #     self.click(self.ITEM_INS_FOLDER)
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.context_click(self.ITEM_INS_FOLDER)
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.wait_is_visible(10, self.ITEMS_INS_CM_NEW)
    #     self.click(self.ITEMS_INS_CM_NEW)
    #     self.driver.implicitly_wait(3)
    #     time.sleep(1)
    #
    #     self.wait_switch_to_frame(5, self.FRAME_ADD_ITEM)
    #
    #     self.write(self.ADD_ITEM_DIALOG__ITEM_TITLE, 'AP-TA Pressure sensor')
    #     #time.sleep(1)
    #     self.write(self.ADD_ITEM_DIALOG__ITEM_DESC, 'AP-TA Pressure transmitter')
    #     #time.sleep(1)
    #
    #     new_item_number = self.get_element_attribute_value(self.ADD_ITEM_DIALOG__ITEM_NUMBER)
    #     self.click(self.ADD_ITEM_DIALOG__SAVE_CLOSE_BUTTON)
    #     time.sleep(1)
    #
    #     self.driver.switch_to.parent_frame()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     # self.switch_to_default()
    #     #time.sleep(1)
    #
    #     self.wait_is_visible(5, self.ITEM_INS_FOLDER)
    #     #time.sleep(1)
    #
    #     self.click(self.ITEM_INS_FOLDER)
    #     time.sleep(1)
    #
    #     self.wait_is_visible(5, self.GRID_LV)
    #     self.click(self.GRID_LV_1st_CELL)
    #
    #     self.wait_is_visible(5, self.DV_ITEM_NUMBER)
    #     dv_item_number = self.get_element_attribute_value(self.DV_ITEM_NUMBER)
    #
    #     self.assertEqual(new_item_number, dv_item_number, 'Found different item numbers')
    #
    # def test_create_new_item(self, item_no='AP_Test_002'):
    #     self.sign_in_admin()
    #     self.select_stack_menu(self.ITEM_STACK_MENU)
    #     self.driver.implicitly_wait(2)
    #     #time.sleep(1)
    #     self.refresh_menu()
    #     self.driver.implicitly_wait(2)
    #     #time.sleep(1)
    #     self.click(self.EXPAND_ITEM_BUTTON)
    #     self.driver.implicitly_wait(2)
    #     #time.sleep(1)
    #     self.click(self.ITEM_INS_FOLDER)
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.context_click(self.ITEM_INS_FOLDER)
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     self.wait_is_visible(10, self.ITEMS_INS_CM_NEW)
    #     self.click(self.ITEMS_INS_CM_NEW)
    #     self.driver.implicitly_wait(3)
    #     time.sleep(1)
    #
    #     self.wait_switch_to_frame(5, self.FRAME_ADD_ITEM)
    #
    #     self.select_and_overwrite(self.ADD_ITEM_DIALOG__ITEM_NUMBER, item_no)
    #
    #     self.write(self.ADD_ITEM_DIALOG__ITEM_TITLE, 'Generic item title')
    #     #time.sleep(1)
    #     self.write(self.ADD_ITEM_DIALOG__ITEM_DESC, 'Generic item description')
    #     #time.sleep(1)
    #
    #     new_item_number = self.get_element_attribute_value(self.ADD_ITEM_DIALOG__ITEM_NUMBER)
    #     self.click(self.ADD_ITEM_DIALOG__SAVE_CLOSE_BUTTON)
    #     time.sleep(1)
    #
    #     self.driver.switch_to.parent_frame()
    #     self.driver.implicitly_wait(2)
    #     time.sleep(1)
    #
    #     # self.switch_to_default()
    #     #time.sleep(1)
    #
    #     self.wait_is_visible(5, self.ITEM_INS_FOLDER)
    #     #time.sleep(1)
    #
    #     self.click(self.ITEM_INS_FOLDER)
    #     time.sleep(1)
    #
    #     self.wait_is_visible(5, self.GRID_LV)
    #     self.click(self.GRID_LV_1st_CELL)
    #
    #     self.wait_is_visible(5, self.DV_ITEM_NUMBER)
    #     dv_item_number = self.get_element_attribute_value(self.DV_ITEM_NUMBER)
    #
    #     self.assertEqual(new_item_number, dv_item_number, 'Found different item numbers')


"""
# iframe Add_item
# //*[@id="RadWindowWrapper_POPUP_FIRST_WINDOW"]/table/tbody/tr[2]/td[2]/iframe

div LV: selector = #ctl00_MCPH_ListView_gridView
xpath = //*[@id="ctl00_MCPH_ListView_gridView"]

prima linie LV: selector = #ctl00_MCPH_ListView_gridView_ctl00__0
xpath = //*[@id="ctl00_MCPH_ListView_gridView_ctl00__0"]


prima celula LV: xpatch = //*[@id="ctl00_MCPH_ListView_gridView_ctl00__0"]/td[2]
selector = #ctl00_MCPH_ListView_gridView_ctl00__0 > td:nth-child(2)


DV Item_number: selector = #MCPH_DetailView_uiWeb_NUMBER_rdTextBox
xpath = //*[@id="MCPH_DetailView_uiWeb_NUMBER_rdTextBox"]

"""
