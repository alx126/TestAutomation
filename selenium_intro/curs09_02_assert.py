import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
########### assert ###########

assert este sintaxa care evalueaza o conditie si returneaza o eroare in cazul in care conditia nu este adevarata

Practic, in testare automata, un assert este cel care decide daca testul e "trecut" sau "picat" (passed sau failed) 
"""

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com/"

driver.get(LINK)

driver.maximize_window()

# CAZ 1 - Verificam daca URL-ul paginii este corect

link_actual = driver.current_url
link_asteptat = LINK

assert link_actual == link_asteptat, f'Invalid URL \n Expected {link_asteptat} but found {link_actual}'

# CAZ 2 - Verificam daca titlul paginii (cel din tab-ul browserului) este afisat corect

titlu_actual = driver.title
titlu_asteptat = "Formy"

assert titlu_actual == titlu_asteptat, f'Invalid title \n Expected {titlu_asteptat} but found {titlu_actual}'

# CAZ 3 - Verificam daca mesajul de welcome din elementul //h1 este afisat corect

mesaj_actual = driver.find_element(By.XPATH, "//h1").text
mesaj_asteptat = "Welcome to Formy"

assert mesaj_actual == mesaj_asteptat, f'Invalid message \n Expected {mesaj_asteptat} but found {mesaj_actual}'


# CAZ 4 - Verificam ca la apasarea butonului "Submit" se afiseaza un mesaj de succes

driver.get("https://formy-project.herokuapp.com/form")
time.sleep(2)


submit_button = driver.find_element(By.XPATH, "//a[text()='Submit']")
submit_button.click()

# implicit wait
driver.implicitly_wait(1)

mesaj_succes = driver.find_element(By.CLASS_NAME, "alert-success")

assert mesaj_succes.is_displayed(), f'Message not displayed!'