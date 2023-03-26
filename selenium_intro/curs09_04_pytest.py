import time
from selenium import webdriver

LINK = "https://formy-project.herokuapp.com/form"

"""
########### pytest ###########

Pytest este un framework de testare care poate fi folosit atat pentru Unit Testing cat si pentru Integration Testing sau 
Functional Testing.

Pentru a rula toate testele dintr-un fisier, se va folosi terminalul

### Teste in mod secvential (unul dupa celalalt):
Pentru a rula testele unul dupa altul, se foloseste comanda:

 pytest calea_catre_fisier/fisier.py     

-> in cazul nostru:     pytest 3_selenium_intro/curs09_04_pytest.py

### Teste in paralel (mai multe deodata):
Pentru a rula teste in paralel, se foloseste comanda:

    pytest calea_catre_fisier/fisier.py -n nr_instante  

    -> in cazul nostru:     pytest 3_selenium_intro/curs09_04_pytest.py -n 2
"""


def test_chrome():
    driver = webdriver.Firefox()
    driver.get(LINK)
    expected_url = "https://formy-project.herokuapp.com/form"
    actual_url = driver.current_url
    time.sleep(10)
    assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"
    driver.quit()


def test_firefox():
    driver = webdriver.Chrome()
    driver.get(LINK)
    expected_url = "https://formy-project.herokuapp.com/form"
    actual_url = driver.current_url
    time.sleep(10)
    assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"
    driver.quit()