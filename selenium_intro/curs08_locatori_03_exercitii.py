from datetime import datetime

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://formy-project.herokuapp.com/datepicker")


# Exercitiu 1: Definim o functie pentru deschiderea date picker-ului pe care o vom refolosi


def open_date_picker():
    if len(driver.find_elements(By.CLASS_NAME, "day")) == 0:
        driver.find_element(By.ID, "datepicker").click()
        time.sleep(1)


# open_date_picker()

# Exercitiu 2: Deschidem date picker-ul si dam click pe ziua curenta
# Ce observam?
# Cum putem sa facem programul sa ruleze corect indiferent data în care suntem?
# Care este diferenta dintre ziua de astazi si celelalte zile ale calendarului?

open_date_picker()

driver.find_element(By.CSS_SELECTOR, ".today.day").click()
time.sleep(2)

# Exercitiu 3: Deschidem date picker-ul si afisam cate zile are luna curenta
# Sa mearga corect indiferent de data in care rulam scriptul

open_date_picker()

# Salvam elementele intr-o lista, apoi afisam marimea listei
zile_luna_curenta = driver.find_elements(By.XPATH, "//td[@class='day' or contains(@class, 'today')]")
print(f"Luna curenta are {len(zile_luna_curenta)} zile")

# Exercitiu 4: Deschidem date picker-ul si afisam TOATE zilele care se vad din luna trecuta
zile_luna_trecuta = driver.find_elements(By.CSS_SELECTOR, ".old.day")
for zi in zile_luna_trecuta:
    print(f"Zi din luna trecuta: {zi.text}")

# Exercitiu 5: Afisam zilele pare care le vedem din luna urmatoare
zile_luna_viitoare = driver.find_elements(By.CSS_SELECTOR, ".new.day")

print("Zile pare luna viitoare:")
for zi in zile_luna_viitoare:
    if int(zi.text) % 2 == 0:
        print(zi.text)


# Exercitiu 6: Navigam in calendar folosind butonul » (Next) pana cand ajungem in anul 2024
def get_calendar_month_year():
    return driver.find_element(By.CLASS_NAME, "datepicker-switch").text


next_button = driver.find_element(By.CLASS_NAME, "next")

while "2024" not in get_calendar_month_year():
    next_button.click()
    time.sleep(1)

# Simulam apasarea butonului ESCAPE ca sa iesim din calendar
time.sleep(1)

# Exercitiu 7: Apasam butonul « (Prev) pana cand ajungem la March 2023
prev_button = driver.find_element(By.CLASS_NAME, "prev")

while "March 2023" not in get_calendar_month_year():
    prev_button.click()
    time.sleep(1)


# Exercitiu 8: Scriem o functie care selecteaza o data din viitor
# Functia va primi 3 parametri (anul, luna - string in limba engleza, ziua)

def select_date(year, month, day):
    open_date_picker()
    while year not in get_calendar_month_year():
        next_button.click()

    while month not in get_calendar_month_year():
        next_button.click()

    driver.find_element(By.XPATH, f"//td[@class='day' and contains(text(), {day})]").click()

select_date("2023", "May", 15)

driver.quit()