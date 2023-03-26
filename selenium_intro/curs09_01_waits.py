import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

"""
########### IMPLICIT WAIT ###########

Aplicatiile web (si nu numai) pot avea mai multe elemente dinamice care apar si dispar in functie de anumite actiuni ale 
utilizatorului. 
Daca driverul incearca sa interactioneze cu un astfel de element inainte ca acesta sa apara, se va returna o eroare, iar 
testele vor fi marcate ca fiid "picate". 

Functia implicitly_wait(x) va face driver-ul sa astepte dupa un element timp de x secunde inainte returnarii unei erori.

ATENTIE: Odata setat, implicitly_wait() se va aplica pe tot parcursul vietii driverului sau pana cand acesta va fi 
schimbat cu un alt implicitly_wait() aplicat pe driver.

"""

# declaram un serviciu - va instala browserul in cazul in care nu exista pe PC
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

LINK = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"

driver.get(LINK)


# Functie care returneaza ora curenta in formatul ora:minut:secunda
def get_time():
    return datetime.now().strftime('%H:%M:%S')


# cu un wait de 5 secunde testul va pica, deoarece elementul devine prezent dupa 10 secunde
# driver.implicitly_wait(5)

driver.implicitly_wait(11)

button_change_text = driver.find_element(By.ID, "populate-text")
button_change_text.click()

print(f"{get_time()}: Incepem asteptarea")
h2_text_selenium_webdriver = driver.find_element(By.XPATH, "//h2[@id='h2' and text()='Selenium Webdriver']")
print(f"{get_time()}: S-a gasit elementul")

assert h2_text_selenium_webdriver.is_displayed()

"""
########### EXPLICIT WAITS ###########

Wait-urile explicite sunt putin diferite de implicit_wait(), deoarece ele se aplica o singura data (in momentul in care
 sunt apelate ca functie) existand mai multe conditii dupa care putem astepta sa fie indeplinite.

Exemple de conditii: 
- prezenta elementului
- vizibilitatea elementului
- elementul sa contina un text
- atributul unui element sa existe
- atributul unui element sa contina o anumita valoare
- etc...

Structura unui explicit wait:

    wait = WebdriverWait(driver, x)
    wait.until(expected_condition)

unde:
WebdriverWait - este clasa care face driverul sa astepte
x - este cantitatea maxima de timp pana la indeplinirea conditiei (si inaintea returnarii unei erori)
expected_condition - conditia dupa care asteptam sa se indeplineasca
"""

# Declaram WebElement pentru butonul care va afisa un alt buton dupa 10 secunde
button_display_button = driver.find_element(By.ID, "display-other-button")

# Click pe buton
button_display_button.click()

# Declaram un WebdriverWait de 10 secunde - aici doar definim wait-ul, asteptarea inca nu incepe
wait = WebDriverWait(driver, 11)

# Deoarece butonul este prezent in DOM, dar este invizibil, va trebui sa asteptam pana cand acesta devine vizibil

print(f"{get_time()}: Incepem asteptarea")

# aici incepem sa asteptam dupa butonul care trebuie sa devina vizibil
wait.until(EC.visibility_of_element_located((By.ID, "hidden")))

print(f"{get_time()}: Elementul a devenit vizibil")

driver.find_element(By.ID, "hidden").click()