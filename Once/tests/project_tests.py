import time
from datetime import datetime
import unittest

from selenium.webdriver.common.by import By

from Once.sites.webdev import WebDev
from Once.utils.driverfactory_Chrome import DriverFactoryChrome
from Once.pages.login_page_webdev import LoginPageWebDev
from Once.menus.project_menu import ProjectMenu
from Once.sites.base_site import BaseSite


class ProjectTests(unittest.TestCase):

    def setUp(self):
        self.driver = DriverFactoryChrome.get_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        self.login_page = LoginPageWebDev(self.driver)
        self.base_site = BaseSite(self.driver)

        self.now = datetime.now()
        self.date_second = datetime.second
        self.date_minute = datetime.minute
        self.date_hour = datetime.hour
        self.date_day = datetime.day
        self.date_month = datetime.month
        self.date_year = datetime.year

    def tearDown(self):
        self.driver.quit()

    def test_select_menu_Project(self):
        # login_page = LoginPageWebDev(self.driver)
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_admin()
        self.driver.find_element(By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[1]').click()
        time.sleep(1)

    def test_create_new_project(self):  #, new_project_number='230428TEST1'
        self.login_page.navigate_to_login_page()
        self.login_page.sign_in_engsys()

        new_project_number = self.now.strftime("%y%m%d_%H%M%S")
        print(f'{new_project_number}')

        self.base_site.select_stack_menu(ProjectMenu.PROJECT_STACK_MENU)
        self.driver.implicitly_wait(2)
        #time.sleep(1)
        self.base_site.refresh_menu(ProjectMenu.REFRESH_MENU_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.click(ProjectMenu.PROJECT_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.context_click(ProjectMenu.PROJECT_FOLDER)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.wait_is_visible(5, ProjectMenu.PROJECT_FOLDER__CM_NEW)
        self.base_site.click(ProjectMenu.PROJECT_FOLDER__CM_NEW)
        self.driver.implicitly_wait(3)
        time.sleep(1)

        self.base_site.wait_switch_to_frame(5, self.base_site.FRAME_NEW_ENTITY)

        self.base_site.write(ProjectMenu.NEW_PROJECT_DIALOG__PROJ_CODE, new_project_number)
        self.base_site.write(ProjectMenu.NEW_PROJECT_DIALOG__PROJ_NAME, new_project_number)
        self.base_site.write(ProjectMenu.NEW_PROJECT_DIALOG__PROJ_MANAGER, ProjectMenu.PROJ_MANAGER_AP)
        self.base_site.write(ProjectMenu.NEW_PROJECT_DIALOG__PROJ_DESC, 'Test new project')
        self.base_site.write(ProjectMenu.NEW_PROJECT_DIALOG__TAG_CODES, ProjectMenu.CODING_STD_NAME)
        self.driver.implicitly_wait(3)
        time.sleep(1)
        self.base_site.click(ProjectMenu.NEW_PROJECT_DIALOG__SAVE_CLOSE_BUTTON)
        self.driver.implicitly_wait(3)
        time.sleep(1)

        self.driver.switch_to.parent_frame()
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.wait_is_visible(5, ProjectMenu.GRID_LV)
        self.base_site.write(ProjectMenu.GRID_LV_FILTER_CODE, new_project_number)
        self.base_site.click(ProjectMenu.GRID_LV_FILTER_BUTTON)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.base_site.click(ProjectMenu.GRID_LV_1st_CELL)

        self.base_site.wait_is_visible(5, ProjectMenu.DV_PROJECT__PROJ_CODE)
        dv_project_number = self.base_site.get_element_attribute_value(ProjectMenu.DV_PROJECT__PROJ_CODE)

        self.assertEqual(new_project_number, dv_project_number, 'Found different project number')


