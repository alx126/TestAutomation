import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com/"
link2 = 'https://formy-project.herokuapp.com/'
LINK1 = "https://the-internet.herokuapp.com/"
'''
driver.get(LINK)
time.sleep(3)
driver.maximize_window()
time.sleep(3)

#cautare dupa Link text
link_web_form = driver.find_element(By.LINK_TEXT, 'Complete Web Form')
link_web_form.click()
time.sleep(2)

driver.back()
time.sleep(2)

#cautare dupa link partial
link_partial_web_form = driver.find_element(By.PARTIAL_LINK_TEXT, 'Web Form')
link_partial_web_form.click()
time.sleep(2)

# ################ 3. TAG NAME
lista_inputuri = driver.find_elements(By.TAG_NAME, "input")
print(f"Avem {len(lista_inputuri)} elemente cu tag-ul HTML <input>")

# for element in lista_inputuri:
#     element.click()
#     time.sleep(1)

# xpath absolut catre elementul de tip input - nu se folosesc pt ca devin fff lungi
#html/body/div/form/div/div[2]/input

# xpath relativ - caut un div care are in interiorul lui...
# cu @ ma refer la atribute
#//div[@id='xxx']
#//input[@id='first-name']/.. - se duce un pas mai sus, pt a gasi parintele inputului cu id ='first-name'

# ################ 4. ID
first_name_input = driver.find_element(By.ID, 'first-name')
assert first_name_input.is_displayed()
first_name_input.click()
time.sleep(1)

# ################ 5. CLASS NAME
lista_elemente_form_control = driver.find_elements(By.CLASS_NAME, 'form-control')
print(f"Avem {len(lista_elemente_form_control)} elemente cu clasa 'form-control'")

# for element in lista_elemente_form_control:
#     element.click()
#     time.sleep(1)

# ################ 6. XPATH

# #### XPATH ABSOLUT - calea absoluta catre element, incepand cu nodul <html>
#first_name_absolut = driver.find_element(By.XPATH, '/html/body/div/form/div/div[1]/input')

driver.back()
time.sleep(2)
link_partial_web_form = driver.find_element(By.PARTIAL_LINK_TEXT, 'Web Form')
link_partial_web_form.click()
time.sleep(2)

first_sau_last_name = driver.find_elements(By.XPATH, '//input[@id="first-name"] | //input[@id="last-name"]')
print(f'Am gasit {len(first_sau_last_name)} elemente.')
for element in first_sau_last_name:
    element.click()
    time.sleep(2)
 '''
#
# driver.get(link2)
# driver.find_element(By.PARTIAL_LINK_TEXT, ' Form').click()
# time.sleep(2)
#
# # selector by CSS - ID
# driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys("An")
# time.sleep(2)
#
# # selector by CSS - Class - only first one if multiple matches
# driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys("dy")
# time.sleep(2)
#
# # selector by CSS - atribut -valoare
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys('S')
# time.sleep(2)
#
# # selector by CSS - atribut-valoare partiale + parinte -> copil
# driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('inpetrean')
# time.sleep(2)

'''
driver.get(LINK1)
driver.maximize_window()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Form Authentication").click()
driver.implicitly_wait(1)
text = driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute('href')

print(f'{text}')
'''
driver.get(LINK1)
driver.maximize_window()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Form Authentication").click()
driver.implicitly_wait(1)

driver.find_element(By.CSS_SELECTOR, 'button.radius[type="submit"]').click()
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, 'div#flash.flash.error')
driver.implicitly_wait(2)
flash_error = driver.find_element(By.CLASS_NAME, "flash.error").text
print(f'{flash_error}')
