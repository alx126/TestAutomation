import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

# ######################### Intro HTML, DOM, CSS #########################

"""
Pagina HTML = orice pagina web scrisa in limbajul HTML

Forma generala a unui fisier html:

<html>      - Nodu HTML, primul nod din document. Marcheaza inceputul paginii.

    <head>
            .... - aici vine metadata neafisata in browser (ex: titlul paginii, fisiere pt stil, etc)
    </head

    <body>
            .... - aici vin elementele din pagina (div-uri, butoane, input-uri, etc)
    </body>

</html>     

Nodul <head> - este un container pentru metadata (date despre date) si poate contine titlul paginii, 
referinte catre fisiere cu scripturi, stiluri si alte

Nodul <body> - contine elementele propriu-zise din pagina care sunt afisate in browser

- Fiecare element din pagina are un tip 
- Aceste tipuri sunt indicate printr-un <tag> HTML
- Orice element care se deschide cu un <tag> trebuie sa se si inchida cu un alt </tag> curespunzator 

Cele mai intalnite tag-uri HTML sunt:

<div> - division = marcheaza inceputul unei diviziuni 
<input> - input = o zona in care se poate introduce un text
<textarea> - text area = asemanator cu inputul, dar mai mare ca dimensiune 
<label> - label = reprezinta o eticheta text care descrie un element sau un grup de elemente
<button> - buton = buton HTML
<td> - tabel = tabel HTML 
<th> - tabel head = cap de tabel tabel 
<tr> - tabel row = rand dintr-un tabel 
<td> - tabel data = o celula dintr-un tabel
<select> - dropdown = lista din care se poate selecta un item dorit
<form> - formular = un formular alcatuit din mai multe elemente 

DOM = Document Object Model - modelul de reprezentare a unei pagini web 
DOM-ul are structura unui tree (copac) si contine toate elementele care se afla intr-o pagina HTML. 

Fiecare element poate avea atribute (proprietati) precum id, class, name, etc. 
- id: de regula este unic pentru fiecare element
- name: este de regula folosit pentru a identifica elementele mai usor in javascript
- class: este folosita de fisierele css care ajuta la stilizarea elementelor

Fisierele javascript sunt incluse de regula in <head> si definesc comportamentul elementelor dintr-o pagina
Fisierele css sunt incluse si ele in <head> ajuta la stilizare 

Pentru a simula navigarea pe internet, avem nevoie si de un browser.
"""

# ######################### INSTALARE SELENIUM SI WEBDRIVE MANAGER #########################

# In terminal scriem urmatoarele randuri, unul cate unul, apasand Enter si asteptand sa se instaleze fiecare

"""
pip install selenium
pip install webdriver-manager
"""

# Documentatiile oficiale ale librariilor:
# Selenium: https://pypi.org/project/selenium/
# webdriver-manager: https://pypi.org/project/webdriver-manager/

"""
NOTA: 

Daca nu merge instalatul package-urilor prin pip install, 

1. Deschideti un terminal powershell (Start-ul din Windows-> tastati powershell -> click dreapta -> Run as Administrator)
si tastati urmatoarea comanda urmata de enter:   Set-ExecutionPolicy Unrestricted 

Sau in PyCharm intram in meniul File -> Settings -> Tools -> Terminal si schimbam Shell path din powershell in CMD

"""

# ######################### CREARE WEBDRIVER SI NAVIGARE CATRE UN LINK #########################

# Vom crea o instanta de WebDriver (tip Chrome) pentru a putea naviga si interactiona cu elemente intr-un browser Chrome
# Browserul se deschide in momentul in care initializam variabila driver

driver = webdriver.Chrome()

# ALTERNATIVA: (varianta cu webdriver manager), folosit in versiuni anterioare de Python (sub 3.7):
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

# Declaram o constanta de tip string cu linkul pe care il vom deschide in browser
LINK = "https://formy-project.herokuapp.com/"

# instructiune pentru a deschide un URL
driver.get(LINK)
time.sleep(1)

# instructiune pentru a maximiza fereastra
driver.maximize_window()

# ######################### TIPURI DE LOCATORI + EXEMPLE #########################

"""
Pentru a putea interactiona cu elementele dintr-o pagina HTML, libraria Selenium vine in ajutorul nostru, oferindu-ne 
posibilitatea de a identifica elementele folosindu-ne de locatorii care acestia ii pot avea

Locator = o modalitate <abstracta> prin care definim cum poate fi identificat un element in DOM

Modalitati prin care putem identifica un WebElement:

- LINK TEXT: un text (exact) care are un link ancorat -> un element cu tag-ul HTML <a> 

- PARTIAL LINK TEXT: un text (parte dintr-un text) care are un link ancorat -> un element cu tag-ul HTML <a> 

- TAG NAME: tag-ul html

- ID: dupa id-ul elementului

- CLASS NAME: atributul class al unui element

- XPATH: calea relativa sau absoluta catre un element in DOM

- CSS SELECTOR: selectorul css
"""

# ################ 1. LINK TEXT
link_web_form = driver.find_element(By.LINK_TEXT, 'Complete Web Form')
link_web_form.click()
time.sleep(2)

# navigam inapoi la pagina anterioara
driver.back()
time.sleep(2)

# varianta gresita - By.LINK_TEXT cere textul exact (textul din element trebuie sa fie egal cu textul introdus)
# link_web_form = driver.find_element(By.LINK_TEXT, 'Web Form')

# ################ 2. PARTIAL LINK TEXT
link_partial_web_form = driver.find_element(By.PARTIAL_LINK_TEXT, 'Web Form')
link_partial_web_form.click()
time.sleep(2)

# ################ 3. TAG NAME
lista_inputuri = driver.find_elements(By.TAG_NAME, "input")
print(f"Avem {len(lista_inputuri)} elemente cu tag-ul HTML <input>")

for element in lista_inputuri:
    element.click()
    time.sleep(1)

# ################ 4. ID
first_name_input = driver.find_element(By.ID, 'first-name')
assert first_name_input.is_displayed()

# ################ 5. CLASS NAME
lista_elemente_form_control = driver.find_elements(By.CLASS_NAME, 'form-control')
print(f"Avem {len(lista_elemente_form_control)} elemente cu clasa 'form-control'")

for element in lista_elemente_form_control:
    element.click()
    time.sleep(1)

# ################ 6. XPATH

# #### XPATH ABSOLUT - calea absoluta catre element, incepand cu nodul <html>

# simbolul / (forward-slash) indica faptul ca ne referim la primul copil al elementului parinte cu tag-ul pe care
# urmeaza sa-l specificam dupa el

# in cazul in care un parinte are mai multi copii cu acelasi <tag>, putem specifica copilul la care ne referim
# indicandu-i ordinea intre paranteze drepte, de exemplu primul div va fi marcat astfel: div[1]
first_name_absolut = driver.find_element(By.XPATH, '/html/body/div/form/div/div[1]/input')

# ##### XPATH RELATIV - o cale relativa in care ne putem folosi de atributele elementului/elementelor la care ne referim

# putem avea un numar variabil de cai relative care sa bata catre acelasi element, depinde de ce vrem sa ne folosim
# caile relative incep cu // si indica faptul ca nu pornim de la primul element din document (adica nodul <html>)
# simbolul " * " indica faptul ca ne referim la toate tipurile de element, indiferent de tag
# dupa specificarea tag-ului html, intre paranteze drepte indicam atributele dupa care vrem sa identificam elementul
# cu @ marcam atributul, apoi ii indicam valoarea EXACTA intre ghilimele

# acelasi element cu XPATH-uri diferite

# xpath relativ care selecteaza toate elementele cu id-ul first-name
first_name_relativ_fara_tag_cu_id = driver.find_element(By.XPATH, '//*[@id="first-name"]')
# xpath relativ care selecteaza toate elementele de tip input si cu id-ul first-name
first_name_relativ_cu_tag_cu_id = driver.find_element(By.XPATH, '//input[@id="first-name"]')
# xpath relativ care selecteaza toate elementele (indiferent de tag) si cu atributul @placeholder avand valoarea "Enter first name"
first_name_relativ_fara_tag_cu_placeholder = driver.find_element(By.XPATH, '//*[@placeholder="Enter first name"]')
# xpath relativ care selecteaza toate elementele de tip input si cu atributul @placeholder avand valoarea "Enter first name"
first_name_relativ_cu_tag_cu_placeholder = driver.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')
print("")

# ################ CSS SELECTOR
"""
 simbolul   *  - selecteaza toate elementele
 sintaxa    #idElement  - selecteaza elementul cu id-ul "idElement"
 .button - selecteaza elementele care au clasa "button" 
 .button.primary - selecteaza elementele care au atat clasa "button" cat si clasa "primary"
 input  - selecteaza toate elementele de tip input
 div input -  selecteaza toate elementele de tip input care se afla intr-un div
 div > input - selecteaza toate elementele de tip input unde parintele e un div
 div + input - selecteaza primul element input care e dupa un element div
 div ~ input - selecteaza toate elementele de tip input precedate de un element div
 input [class] - selecteaza elementele de tip input care au atributul class
 input [class='value'] - selecteaza elementele de tip input care au atributul class = 'value'
 input [class~='value'] - selecteaza elementele de tip input ale caror atribut class contine textul 'value' 
 [id|="radio-button"] - selecteaza toate elementele ale caror id e egal cu sau incepe cu radio-button
"""

# ##### acelasi element cu CSS-uri diferite

# doar cu #ID
first_name_cu_id_css = driver.find_element(By.CSS_SELECTOR, '#first-name')
# tag si #ID
first_name_cu_tag_si_id_css = driver.find_element(By.CSS_SELECTOR, 'input#first-name')
# tag si ID, de data asta ca id-ul e mentionat la fel ca orice alt atribut si fara #
first_name_cu_tag_si_atribut_id_css = driver.find_element(By.CSS_SELECTOR, 'input[id="first-name"]')
# tag si atributul placeholder
first_name_cu_tag_si_atribut_placeholder_css = driver.find_element(By.CSS_SELECTOR,
                                                                   'input[placeholder="Enter first name"]')
# tag cu clasa si atributul id
first_name_cu_tag_clasa_si_id = driver.find_element(By.CSS_SELECTOR, 'input.form-control[id="first-name"]')

# element cu tag-ul input si atributul type = radio
radio_cu_atribut_type_radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")

# ######################### PROPRIETATILE SI METODELE UNUI WEBELEMENT #########################


"""
WebElement = un WebElement reprezinta un element dintr-o pagina HTML.

Obiectul (variabila) care reprezinta un Web Element nu e altceva decat o referinta catre acel element.

Daca se face un refresh pe pagina sau daca elementul se reincarca,
referintele pot deveni invalide si primim un StaleElementReferenceException
"""

# DEMO StaleElementReferenceException
# Navigam inapoi si incercam sa facem click pe linkul 'Complete Web Form' salvat in variabila link_web_form
driver.back()

try:
    link_web_form.click()  # incercand sa facem click pe link_web_form, vom primi un StaleElementReferenceException
except StaleElementReferenceException as eroare:
    print("Avem un StaleElementReferenceException, elementul <<a expirat>> ")
    print(eroare.msg)

# la final e important sa inchidem driverul, altfel poate ramane deschis
# ca proces fantoma in fundal si sa consume memorie fara sa stim
driver.quit()
