#Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
#● Id
#● Link text
#● Parțial link text
#● Name
#● Tag*
#● Class name*
#● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

LINK1 = "https://formy-project.herokuapp.com/"
LINK2 = "https://www.phptravels.net/"
LINK3 = "http://automationpractice.com/index.php"
LINK4 = "https://the-internet.herokuapp.com/"
LINK5 = "https://www.techlistic.com/p/selenium-practice-form.html"
LINK6 = 'https://jules.app'


# ID
driver.get(LINK2)
time.sleep(1)
driver.maximize_window()
time.sleep(1)

tab_flight = driver.find_element(By.ID, "flights-tab")
assert tab_flight.is_displayed(), 'Elementul nu apare'
time.sleep(1)
tab_flight.click()
time.sleep(1)

tab_tours = driver.find_element(By.ID, "tours-tab")
assert tab_tours.is_displayed(), 'Elementul nu apare'
time.sleep(1)
tab_tours.click()
time.sleep(1)

tab_cars = driver.find_element(By.ID, "cars-tab")
assert tab_cars.is_displayed(), 'Elementul nu apare'
time.sleep(1)
tab_cars.click()
time.sleep(1)

tab_flight.click()
time.sleep(2)

# radio_butoane = driver.find_elements(By.NAME, 'form-check-input')
# for buton in radio_butoane:
#     buton.click()
#     time.sleep(1)
radio_buton = driver.find_element(By.CSS_SELECTOR, 'input.form-check-input[id="round-trip"]')
radio_buton.click()
time.sleep(1)

fly_from = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Flying From"]')
fly_from.send_keys('Henri Coanda')
time.sleep(1)

driver.find_element(By.XPATH, '//strong[contains(text(),"Henri Coanda")]').click()
time.sleep(1)

fly_to = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="To Destination"]')
fly_to.send_keys('Frankfurt')
time.sleep(1)

driver.find_element(By.XPATH, '//strong[contains(text()," Frankfurt Main")]').click()
time.sleep(1)

depart_calendar = driver.find_element(By.CSS_SELECTOR, 'input#departure')
depart_calendar.click()
time.sleep(3)


def get_calendar_month_year():
    return driver.find_element(By.XPATH, "//div[@class='datepicker dropdown-menu']/descendant::th[@class='switch']").text

# right_button = driver.find_element(By.CSS_SELECTOR, 'i.icon.mdi.mdi-long-arrow-right')
# right_button.click()
# time.sleep(1)

right_button = driver.find_element(By.CSS_SELECTOR, 'th.next i')
right_button.click()
time.sleep(1)

left_button = driver.find_element(By.CSS_SELECTOR, 'th.prev i')
left_button.click()
time.sleep(1)

# while "April 2023" not in get_calendar_month_year():
#     right_button.click()
#     time.sleep(1)


#depart_day = driver.find_element(By.CSS_SELECTOR, '')




'''
# Link text
driver.get(LINK4)
time.sleep(1)

link_web_1 = driver.find_element(By.LINK_TEXT, 'A/B Testing')
link_web_1.click()
time.sleep(1)

driver.back()
time.sleep(1)

link_web_2 = driver.find_element(By.LINK_TEXT, 'Add/Remove Elements')
link_web_2.click()
time.sleep(1)

driver.back()
time.sleep(1)

link_web_3 = driver.find_element(By.LINK_TEXT, 'Form Authentication')
link_web_3.click()
time.sleep(1)

driver.back()
time.sleep(1)

# Partal link text

link_partial_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Content")
link_partial_1.click()
time.sleep(1)

driver.back()
time.sleep(1)

link_partial_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Disappearing")
link_partial_2.click()
time.sleep(1)

driver.back()
time.sleep(1)

link_partial_3 = driver.find_element(By.PARTIAL_LINK_TEXT, "Alerts")
link_partial_3.click()
time.sleep(1)

driver.back()
time.sleep(1)
'''
'''
# Name
link_web_3 = driver.find_element(By.LINK_TEXT, 'Form Authentication')
link_web_3.click()
time.sleep(1)

user_name = driver.find_element(By.NAME, 'username')
user_name.click()
user_name.send_keys('tomsmith')
time.sleep(1)

user_name.()
user_name.click()
time.sleep(1)
password = driver.find_element(By.NAME, 'password')
password.send_keys('SuperSecretPassword!')
time.sleep(1)

login = driver.find_element(By.TAG_NAME, 'button')
login.click()
time.sleep(1)

logout = driver.find_element(By.CSS_SELECTOR, 'a.button.secondary.radius').click()
time.sleep(5)
'''
'''
# Tag name

driver.get(LINK1)
#time.sleep(1)
driver.maximize_window()
#time.sleep(1)
link_partial_web_form = driver.find_element(By.PARTIAL_LINK_TEXT, 'Web Form').click()
time.sleep(1)

lista_select = driver.find_elements(By.TAG_NAME, "select")
print(f"Avem {len(lista_select)} elemente cu tag-ul HTML <select>")

lista_select[0].click()
time.sleep(3)

lista_input = driver.find_elements(By.TAG_NAME, 'input')
lista_input[0].send_keys('Alexandru')
time.sleep(1)
lista_input[1].send_keys('Parepa')
time.sleep(1)
lista_input[2].send_keys('Project manager')
time.sleep(4)
'''
'''
# Class name

driver.get(LINK2)
#time.sleep(1)
driver.maximize_window()
#time.sleep(1)


# CSS (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
'''
# Pentru xpath identifică elemente după criteriile de mai jos:
# ● 3 după atribut valoare
# ● 3 după textul de pe element
# ● 1 după parțial text
# ● 1 cu SAU, folosind pipe |
# ● 1 cu *
# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
# cu (xpath)[1]
# ● 1 în care să folosești parent::
# ● 1 în care să folosești fratele anterior sau de după (la alegere)
# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
# ce element vreau să interacționez.

