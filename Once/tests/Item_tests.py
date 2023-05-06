import time
from datetime import datetime
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Once.sites.webdev import WebDev
from Once.utils.driverfactory_Chrome import DriverFactoryChrome
from Once.pages.login_page_webdev import LoginPageWebDev
from Once.menus.Item_menu import ItemMenu
from Once.sites.base_site import BaseSite


class ItemTests(unittest.TestCase):

    # LOGGED_USER_BUTTON = (By.CSS_SELECTOR, 'span#textLoginName')
    # ITEM_STACK_MENU = (By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[4]')
    # REFRESH_MENU_BUTTON = (By.CSS_SELECTOR, 'span#rpText.rpText')
    # EXPAND_ITEM_BUTTON = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/div/span[2]')
    # ITEM_INS_FOLDER = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li[9]/div/span[3]')
    # ITEMS_INS_CM_NEW = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[1]/a/span')
    #
    # ADD_ITEM_DIALOG__ITEM_NUMBER = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_NUMBER_rdTextBox"]')
    # ADD_ITEM_DIALOG__ITEM_TITLE = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_ITEM_TITLE_rdTextBox"]')
    # ADD_ITEM_DIALOG__ITEM_DESC = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_ITEM_DESC_rdTextBox"]')
    # ADD_ITEM_DIALOG__SAVE_CLOSE_BUTTON = (By.XPATH, '//*[@id="DVTopMenu"]/li[2]/span/span')
    #
    # FRAME_ADD_ITEM = (By.XPATH, '//*[@id="RadWindowWrapper_POPUP_FIRST_WINDOW"]/table/tbody/tr[2]/td[2]/iframe')
    #
    # GRID_LV = (By.CSS_SELECTOR, '#ctl00_MCPH_ListView_gridView')
    # GRID_LV_1st_CELL = (By.CSS_SELECTOR, '#ctl00_MCPH_ListView_gridView_ctl00__0')
    #
    # DV_ITEM_NUMBER = (By.CSS_SELECTOR, '#MCPH_DetailView_uiWeb_NUMBER_rdTextBox')

    def setUp(self):
        self.driver = DriverFactoryChrome.get_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        time.sleep(1)
        self.login_page = LoginPageWebDev(self.driver)
        self.base_site = BaseSite(self.driver)
        self.item_menu = ItemMenu(self.driver)

        self.now = datetime.now()
        self.date_second = datetime.second
        self.date_minute = datetime.minute
        self.date_hour = datetime.hour
        self.date_day = datetime.day
        self.date_month = datetime.month
        self.date_year = datetime.year

    def tearDown(self):
        self.driver.quit()

    def test_sign_in_admin(self):
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()
        self.assertEqual(self.driver.current_url, WebDev.WEBDEV_URL)
        time.sleep(1)
        user = 'Admin'
        self.base_site.wait_is_visible(5, self.item_menu.LOGGED_USER_BUTTON)
        logged_user = self.base_site.find(self.item_menu.LOGGED_USER_BUTTON).text
        self.assertEqual(logged_user, user, 'Different user logged in.')

    @unittest.skip
    def test_sign_in_EngSys(self):
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_engsys()
        self.driver.implicitly_wait(5)
        self.assertEqual(self.driver.current_url, WebDev.WEBDEV_URL)

    def test_iterate_through_menus(self):
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()
        time.sleep(2)
        menus_list = self.driver.find_elements(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li')

        for i in range(1, len(menus_list)):
            self.base_site.click((By.XPATH, f'//*[@id="BarMenu"]/ul/descendant::li[{i}]'))
            self.driver.implicitly_wait(3)
            time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[1]').click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[2]').click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[3]').click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[4]').click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[5]').click()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[6]').click()
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[7]').click()
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[8]').click()
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[9]').click()
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.driver.back()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        product_menu = self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/li[2]/a/span/span[2]').text
        # //*[@id="BarMenu"]/ul/li[2]/a/span/span[2]/text()

    @unittest.skip
    def test_document_menu_iterate_folders(self):
        login_page = LoginPageWebDev(self.driver)
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()

    def test_create_new_item_instrument(self):
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()
        self.base_site.select_stack_menu(ItemMenu.ITEM_STACK_MENU)
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.base_site.refresh_menu(ItemMenu.REFRESH_MENU_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.base_site.click(ItemMenu.EXPAND_ITEM_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.base_site.click(ItemMenu.ITEM_INS_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.context_click(ItemMenu.ITEM_INS_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.wait_is_visible(10, ItemMenu.ITEMS_INS_CM__NEW)
        self.base_site.click(ItemMenu.ITEMS_INS_CM__NEW)
        self.driver.implicitly_wait(3)
        time.sleep(1)

        self.base_site.wait_switch_to_frame(5, ItemMenu.FRAME_ADD_ITEM)

        self.base_site.write(ItemMenu.ADD_ITEM_DIALOG__ITEM_TITLE, 'AP-TA Pressure sensor')
        # time.sleep(1)
        self.base_site.write(ItemMenu.ADD_ITEM_DIALOG__ITEM_DESC, 'AP-TA Pressure transmitter')
        # time.sleep(1)

        new_item_number = self.base_site.get_element_attribute_value(ItemMenu.ADD_ITEM_DIALOG__ITEM_NUMBER)
        self.base_site.click(ItemMenu.ADD_ITEM_DIALOG__SAVE_AND_CLOSE_BUTTON)
        time.sleep(1)

        self.driver.switch_to.parent_frame()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        # self.switch_to_default()
        # time.sleep(1)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_INS_FOLDER)
        # time.sleep(1)

        self.base_site.click(ItemMenu.ITEM_INS_FOLDER)
        time.sleep(1)

        self.base_site.wait_is_visible(5, ItemMenu.GRID_LV)
        self.base_site.click(ItemMenu.GRID_LV_1st_CELL)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_DV__ITEM_NUMBER)
        dv_item_number = self.base_site.get_element_attribute_value(ItemMenu.ITEM_DV__ITEM_NUMBER)

        self.assertEqual(new_item_number, dv_item_number, 'Found different item numbers')

    def test_create_new_item_with_no(self, item_no='AP_Test_230428_1'):
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()
        self.base_site.select_stack_menu(ItemMenu.ITEM_STACK_MENU)
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.base_site.refresh_menu(ItemMenu.REFRESH_MENU_BUTTON)
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.base_site.click(ItemMenu.EXPAND_ITEM_BUTTON)
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.base_site.click(ItemMenu.ITEM_INS_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.context_click(ItemMenu.ITEM_INS_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.wait_is_visible(10, ItemMenu.ITEMS_INS_CM__NEW)
        self.base_site.click(ItemMenu.ITEMS_INS_CM__NEW)
        self.driver.implicitly_wait(3)
        time.sleep(1)

        self.base_site.wait_switch_to_frame(5, ItemMenu.FRAME_ADD_ITEM)

        item_no = self.now.strftime("AP_%y%m%d_%H%M%S")
        print(f'{item_no}')

        self.base_site.select_and_overwrite(ItemMenu.ADD_ITEM_DIALOG__ITEM_NUMBER, item_no)

        self.base_site.write(ItemMenu.ADD_ITEM_DIALOG__ITEM_TITLE, 'Generic item title')
        # time.sleep(1)
        self.base_site.write(ItemMenu.ADD_ITEM_DIALOG__ITEM_DESC, 'Generic item description')
        # time.sleep(1)

        new_item_number = self.base_site.get_element_attribute_value(ItemMenu.ADD_ITEM_DIALOG__ITEM_NUMBER)
        self.base_site.click(ItemMenu.ADD_ITEM_DIALOG__SAVE_AND_CLOSE_BUTTON)
        time.sleep(1)

        self.driver.switch_to.parent_frame()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_INS_FOLDER)
        self.base_site.click(ItemMenu.ITEM_INS_FOLDER)
        time.sleep(1)

        self.base_site.wait_is_visible(5, ItemMenu.GRID_LV)
        self.base_site.select_and_overwrite(ItemMenu.GRID_LV_FILTER_NUMBER, new_item_number)
        self.base_site.click(ItemMenu.GRID_LV_FILTER_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.base_site.wait_is_visible(5, ItemMenu.GRID_LV)
        self.base_site.click(ItemMenu.GRID_LV_1st_CELL)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_DV__ITEM_NUMBER)
        dv_item_number = self.base_site.get_element_attribute_value(ItemMenu.ITEM_DV__ITEM_NUMBER)

        self.assertEqual(new_item_number, dv_item_number, 'Found different item numbers')

    @unittest.skip
    def test_delete_item(self):
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()
        self.login_page.select_stack_menu(ItemMenu.ITEM_STACK_MENU)
        self.driver.implicitly_wait(2)
        # time.sleep(1)
        self.base_site.refresh_menu(ItemMenu.REFRESH_MENU_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.click(ItemMenu.ITEMS_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.click(ItemMenu.ITEMS_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.click(ItemMenu.GRID_LV_FILTER_NUMBER)
        self.base_site.write(ItemMenu.GRID_LV_FILTER_NUMBER, 'AP_')
        self.base_site.click(ItemMenu.GRID_LV_FILTER_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.wait_is_visible(5, ItemMenu.GRID_LV)
        self.base_site.click(ItemMenu.GRID_LV_1st_CELL)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_DV__ITEM_NUMBER)
        dv_item_number = self.base_site.get_element_attribute_value(ItemMenu.ITEM_DV__ITEM_NUMBER)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_DV__BUTTON_DELETE)
        self.base_site.click(ItemMenu.ITEM_DV__BUTTON_DELETE)
        time.sleep(1)
        self.base_site.confirm_action_click_cancel()
        time.sleep(3)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_DV__BUTTON_DELETE)
        self.base_site.click(ItemMenu.ITEM_DV__BUTTON_DELETE)
        time.sleep(1)
        self.base_site.confirm_action_click_ok()
        time.sleep(3)

        self.base_site.wait_is_visible(5, ItemMenu.GRID_LV)
        self.base_site.click(ItemMenu.GRID_LV_FILTER_NUMBER)
        self.base_site.select_and_overwrite(ItemMenu.GRID_LV_FILTER_NUMBER, dv_item_number)
        self.base_site.click(ItemMenu.GRID_LV_FILTER_BUTTON)
        self.driver.implicitly_wait(2)
        self.assertTrue(ItemMenu.GRID_LV_NO_RECORDS)

    def test_item_link_file_existing(self):
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()
        self.login_page.select_stack_menu(ItemMenu.ITEM_STACK_MENU)
        self.driver.implicitly_wait(2)

        self.base_site.refresh_menu(ItemMenu.REFRESH_MENU_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.click(ItemMenu.ITEMS_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.click(ItemMenu.GRID_LV_FILTER_NUMBER)
        self.base_site.write(ItemMenu.GRID_LV_FILTER_NUMBER, 'AP_')
        self.base_site.click(ItemMenu.GRID_LV_FILTER_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.wait_is_visible(5, ItemMenu.GRID_LV)
        self.base_site.click(ItemMenu.GRID_LV_1st_CELL)

        self.base_site.wait_is_visible(5, ItemMenu.ITEM_DV__ITEM_NUMBER)
        dv_item_number = self.base_site.get_element_attribute_value(ItemMenu.ITEM_DV__ITEM_NUMBER)

        self.base_site.context_click(ItemMenu.GRID_LV_1st_CELL)
        self.base_site.wait_is_visible(5, ItemMenu.ITEM_CM__LINK_FILE)
        self.base_site.click(ItemMenu.ITEM_CM__LINK_FILE)
        self.driver.implicitly_wait(3)

        self.base_site.wait_switch_to_frame(5, ItemMenu.FRAME_UPLOAD_FILES)
        self.driver.implicitly_wait(3)
        time.sleep(1)

        tab_existing = self.driver.find_element(By.XPATH, '//*[@id="tabstrip-tab-1"]')
        print(f'Tab existing element: {tab_existing}')
        time.sleep(1)
        tab_existing.click()

        # self.base_site.click((By.XPATH, '//*[@id="tabstrip-tab-1"]'))

        # self.base_site.wait_for_element_to_be_present(ItemMenu.UPLOAD_FILES_DIALOG__TAB_EXISTING, 5)
        # self.base_site.click(ItemMenu.UPLOAD_FILES_DIALOG__TAB_EXISTING)
        self.driver.implicitly_wait(1)
        time.sleep(1)
        self.base_site.click(ItemMenu.UPLOAD_FILES_DIALOG__EXISTING__GRID_LV_1_CELL)  # /html/body/div[1]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[1]  //tbody[@role="rowgroup"]/tr[1]/td[1]
        time.sleep(1)
        #
        # ActionChains(self.driver).move_to_element(ItemMenu.UPLOAD_FILES_DIALOG__TAB_EXISTING).click().perform()
        # self.driver.implicitly_wait(2)

        # file_name = self.base_site.get_element_attribute_value(
        # (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[1]'))
        file_name = self.driver.find_element(*ItemMenu.UPLOAD_FILES_DIALOG__EXISTING__GRID_LV_1_CELL).text

        print(f'{file_name}')

        self.base_site.click((By.XPATH,
                              '//*[@id="btnSaveExistingFiles"]'))  # //*[@id="btnSaveExistingFiles"] '//*[@id="btnSaveExistingFiles"]/span/span'
        self.driver.implicitly_wait(1)
        time.sleep(2)

        self.driver.switch_to.parent_frame()
        self.driver.implicitly_wait(1)
        time.sleep(2)

        # self.base_site.click(ItemMenu.GRID_LV_FILTER_NUMBER)
        # self.base_site.write(ItemMenu.GRID_LV_FILTER_NUMBER, dv_item_number)
        # self.base_site.click(ItemMenu.GRID_LV_FILTER_BUTTON)
        # self.driver.implicitly_wait(2)
        # time.sleep(1)

        self.base_site.click(ItemMenu.ITEM_DV__TAB_FILE)
        time.sleep(1)

        files_list = self.driver.find_elements(*ItemMenu.UPLOAD_FILES_DIALOG__EXISTING__FILES_LIST)
        # self.find(locator).get_attribute("value")
        for i in range(1, len(files_list)):
            name = self.driver.find_element(By.XPATH, f'//div['
                                                      f'@id="MCPH_DetailView_detailViewLeftPane'
                                                      f'"]/div/div/div/div['
                                                      f'@id="kendoParentGrid"]/div/div/table'
                                                      f'/tbody[@role="rowgroup"]/tr[{i}]/td[1]').text
            if name[i] == file_name:
                print(f'File {name[i]} was linked successfully.')
                self.assertNotEqual(name[i], file_name)
                #break

        #print(f'File {file_name} was linked successfully.')



"""

//*[@id="c7355012-7ab8-4f11-975e-26f8e366919a"]/tr[1]/td[1]
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
