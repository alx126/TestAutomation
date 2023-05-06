import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Once.sites.webdev import WebDev


class ProjectMenu(WebDev):

    CODING_STD_NAME = 'Z-DP-002 R3'
    PROJ_MANAGER_AP = 'AP/Alex Parepa'

    PROJECT_STACK_MENU = (By.XPATH, '//*[@id="BarMenu"]/ul/descendant::li[1]')

    REFRESH_MENU_BUTTON = (By.CSS_SELECTOR, 'span#rpText.rpText')

    PROJECT_FOLDER = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/div/span[3]')
    PROJECT_FOLDER__CM_NEW = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[1]/a/span')

    GRID_LV_FILTER_CODE = (By.XPATH, '//*[@id="ctl00_MCPH_ListView_gridView_ctl00_ctl02_ctl03_FilterTextBox_PROJECT_CODE"]') #css = '#ctl00_MCPH_ListView_gridView_ctl00_ctl02_ctl03_FilterTextBox_PROJECT_CODE'
    GRID_LV_ISOLATE = (By.XPATH, '//*[@id="ctl00_MCPH_ListView_gridView_ctl00_ctl04_gbccolExpand"]')
    GRID_LV_1st_CELL = (By.XPATH, '//*[@id="ctl00_MCPH_ListView_gridView_ctl00__0"]/td[3]')

    TREE_ISOLATED_PROJECT = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li/div/span[3]')
    TREE_ISOLATED_PROJECT_EXPAND = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li/div/span[2]')
    TREE_ISOLATED_PROJECT__TAGS_FOLDER = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li/ul/li[3]/div/span[3]')
    TREE_ISOLATED_PROJECT__TAGS_FOLDER_EXPAND = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li/ul/li[3]/div/span[2]')
    TREE_ISOLATED_PROJECT__PRODUCTS_FOLDER = (By.XPATH, '///*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li/ul/li[9]/div/span[3]')
    TREE_ISOLATED_PROJECT__PRODUCTS_FOLDER_EXPAND = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li/ul/li[9]/div/span[2]')

    TREE_ISOL_PROJ_CM_NEW_TAG = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[6]/a/span')
    TREE_ISOL_PROJ_CM_NEW_TAG__TAG = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[6]/div/ul/li[1]/a/span')
    TREE_ISOL_PROJ_CM_NEW_TAG__INS = (By.XPATH, '//*[@id="DefaultContextMenu_detached"]/ul/li[6]/div/ul/li[10]/a/span')

    FRAME_NEW_PROJECT = (By.XPATH, '//*[@id="RadWindowWrapper_POPUP_FIRST_WINDOW"]/table/tbody/tr[2]/td[2]/iframe')
    FRAME_NEW_TAG = (By.XPATH, '//*[@id="RadWindowWrapper_POPUP_FIRST_WINDOW"]/table/tbody/tr[2]/td[2]/iframe')

    NEW_PROJECT_DIALOG__PROJ_CODE = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_PROJECT_CODE_rdTextBox"]')
    NEW_PROJECT_DIALOG__PROJ_NAME = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_PROJECT_NAME_rdTextBox"]')
    NEW_PROJECT_DIALOG__PROJ_DESC = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_PROJECT_DESC_rdTextBox"]')
    NEW_PROJECT_DIALOG__TAG_CODES = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_RV_CODE_STD_rdTextBox_Input"]')
    NEW_PROJECT_DIALOG__PROJ_MANAGER = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_PERSON_PROJ_MAN_rdTextBox_Input"]')

    NEW_PROJECT_DIALOG__SAVE_CLOSE_BUTTON = (By.XPATH, '//*[@id="DVTopMenu"]/li[2]/span/span')


    NEW_TAG_DIALOG__SAVE_BUTTON = (By.XPATH, '//*[@id="DVTopMenu"]/li[1]/span/span')  # 2 found
    NEW_TAG_DIALOG__SAVE_CLOSE_BUTTON = (By.XPATH, '//*[@id="DVTopMenu"]/li[2]/span/span')  # 2 found # css = '#DVTopMenu > li:nth-child(2) > span > span

    NEW_TAG_DIALOG__PRODUCT = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_PROJECT_BOM_rdTextBox_Input"]')
    NEW_TAG_DIALOG__PRODUCT_ARROW = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_PROJECT_BOM_rdTextBox"]/table/tbody/tr/td[2]')

    NEW_TAG_DIALOG__PRODUCT_OPT_NEW = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_PROJECT_BOM_rdTextBox_Footer"]/div/span/b')
    NEW_TAG_DIALOG__NEW_PRODUCT_WINDOW = (By.XPATH, '//*[@id="RadWindowWrapper_POPUP_FIRST_WINDOW"]')
    NEW_TAG_DIALOG__NEW_PRODUCT__PROD_CODE = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_RV_PRODUCT_rdTextBox_Input"]')
    NEW_TAG_DIALOG__NEW_PRODUCT__INSTANCE_CODE = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_RV_INSTANCE_rdTextBox_Input"]')
    NEW_TAG_DIALOG__NEW_PRODUCT__PROD_DESC = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_DESCRIPTION_rdTextBox"]')
    NEW_TAG_DIALOG__NEW_PRODUCT__SAVE_CLOSE_BUTTON = (By.XPATH, '//*[@id="DVTopMenu"]/li[2]/span/span')  # 3 found

    NEW_TAG_DIALOG__TAG = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_TAG_NO_rdTextBox"]')
    NEW_TAG_DIALOG__TAG_DESC = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_TAG_DESC_rdTextBox"]')
    NEW_TAG_DIALOG__ITEM_NO = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_ITEM_rdTextBox_Input"]')
    NEW_TAG_DIALOG__ITEM_NO_ARROW = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_RUID_ITEM_rdTextBox_Arrow"]')
    NEW_TAG_DIALOG__QTY = (By.XPATH, '//*[@id="ctl00_DetailContent_detailView_uiWeb_QTY_rdTextBox"]')
    NEW_TAG_DIALOG__QTY_UNIT = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_RUID_RV_UNIT"]')
    NEW_TAG_DIALOG__QTY_UNIT_OPT_2 = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_RUID_RV_UNIT"]/option[2]')
    NEW_TAG_DIALOG__QTY_UNIT_OPT_34_METER = (By.XPATH, '//*[@id="DetailContent_detailView_uiWeb_RUID_RV_UNIT"]/option[34]')

    TREE_TAG_UNDER_PROJECT = (By.XPATH, '//*[@id="ctl00_TopLeftPlaceHolder_TreeView"]/ul/li[2]/ul/li/ul/li/div/span[3]')

    DV_TAG__TAG_NO = (By.XPATH, '//*[@id="MCPH_DetailView_uiWeb_TAG_NO_rdTextBox"]')

    DV_PROJECT__PROJ_CODE = (By.XPATH, '//*[@id="MCPH_DetailView_uiWeb_PROJECT_CODE_rdTextBox"]')

    NEW_TAG_DIALOG__NOTIF_REQ_FIELD = (By.XPATH, '//*[@id="eafe2cc4-7064-4103-8928-9d3e0abab7cf"]')

    def __init__(self, driver: webdriver):
        super().__init__(driver)




