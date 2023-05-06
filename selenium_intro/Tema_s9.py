import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login(unittest.TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"
    LOGIN_ERROR = (By.CSS_SELECTOR, ".flash.error")
    LOGIN_SUCCESS = (By.CLASS_NAME, 'flash.success')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.radius[type="submit"]')
    CLOSE_BUTTON = (By.XPATH, "//div[@data-alert]/descendant::a[@class='close']")

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

    def wait_for_element_to_be_absent(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until_not(EC.presence_of_element_located(element_locator))

    def is_element_present(self, element_locator):
        return len(self.driver.find_elements(*element_locator)) > 0

    def login(self, user, password):
        self.driver.find_element(By.ID, 'username').send_keys(user)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def setUp(self):
        print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(1)

    def tearDown(self):
        print(f"Se executa ce este in tearDown() pentru {self._testMethodName}\n")
        self.driver.quit()

    # Verifică dacă noul url e corect
    # @unittest.skip
    def test_url(self):
        print(f"A inceput testul {self._testMethodName}")

        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Invalid URL")

    # Verifică dacă page title e corect
    # @unittest.skip
    def test_title(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_title = 'The Internet'
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Invalid title, expected {expected_title}, but found {actual_title}"
        self.assertEqual(expected_title, actual_title,
                         f"Invalid title, expected {expected_title}, found {actual_title}")

    # Verifică textul de pe elementul xpath=//h2 e corect
    # @unittest.skip
    def test_h2_text(self):
        print(f'A inceput testul {self._testMethodName}')
        expected_text = 'Login Page'
        actual_text = self.driver.find_element(By.XPATH, '//h2').text
        self.assertEqual(expected_text, actual_text, f'Invalid text, expected {expected_text}, found {actual_text}')

    # Verifică dacă butonul de login este displayed
    # @unittest.skip
    def test_buton_login(self):
        print(f'A inceput testul {self._testMethodName}')
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button.radius[type="submit"]')
        assert login_button.is_displayed(), f'Butonul nu este afisat'
        self.assertTrue(login_button.is_displayed(), 'Butonul nu este afisat')

    # Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    # @unittest.skip
    def test_atribut_href(self):
        print(f'A inceput testul {self._testMethodName}')
        expected_atribute = 'http://elementalselenium.com/'
        actual_atribute = self.driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute('href')
        assert expected_atribute == actual_atribute, 'Atributul nu e corect.'
        self.assertEqual(actual_atribute, expected_atribute, 'Atributul nu e corect.')

    # - Lasă goale user și pass
    # - Click login
    # - Verifică dacă eroarea e displayed
    # @unittest.skip
    def test_error_login1(self):
        print(f'A inceput testul {self._testMethodName}')
        expected = f'Your username is invalid!\n×'  # f'Your username is invalid!\n×'

        self.driver.find_element(By.CSS_SELECTOR, 'button.radius[type="submit"]').click()
        self.driver.implicitly_wait(1)
        actual = self.driver.find_element(By.CLASS_NAME, "flash.error")  # (By.CSS_SELECTOR, 'div#flash.flash.error')

        self.assertTrue(actual.is_displayed(), 'Mesajul nu s-a afisat.')
        self.assertEqual(expected, actual.text,
                         f'Mesajul asteptat {expected} e diferit de mesajul afisat {actual.text}.')

    # Completează cu user și pass invalide
    # - Click login
    # - Verifică dacă mesajul de pe eroare e corect
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    # expected = 'Your username is invalid!'
    # self.assertTrue(expected in actual, 'Error message text is
    # incorrect')
    # @unittest.skip
    def test_error_login2(self):
        print(f'A inceput testul {self._testMethodName}')
        expected = 'Your username is invalid!'

        self.driver.find_element(By.ID, 'username').send_keys('username')
        self.driver.find_element(By.ID, 'password').send_keys('password')
        WebDriverWait(self.driver, 3)
        self.driver.find_element(By.CSS_SELECTOR, 'button.radius[type="submit"]').click()
        self.driver.implicitly_wait(3)

        actual = self.driver.find_element(By.CLASS_NAME,
                                          "flash.error").text  # (By.CSS_SELECTOR, 'div#flash.flash.error')(By.CLASS_NAME, "flash.error")
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    # Test 8
    # - Lasă goale user și pass
    # - Click login
    # - Apasă x la eroare
    # - Verifică dacă eroarea a dispărut
    # @unittest.skip
    def test_check_error_login(self):
        print(f'A inceput testul {self._testMethodName}')

        login_button = self.wait_for_element_to_be_present(self.LOGIN_BUTTON, 1)
        login_button.click()

        close_button = self.wait_for_element_to_be_present(self.CLOSE_BUTTON, 2)
        close_button.click()

        wait = WebDriverWait(self.driver, 1)
        no_error = wait.until(EC.invisibility_of_element(self.LOGIN_ERROR))

        self.assertTrue(no_error, "Eroarea este inca afisata.")

    # Test 9
    # - Ia ca o listă toate //label
    # - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
    # Password)
    # - Aici e ok să avem 2 asserturi
    # @unittest.skip
    def test_check_label(self):
        print(f'Am inceput testul {self._testMethodName}')
        expected_labels = ['Username', 'Password']

        labels = self.driver.find_elements(By.TAG_NAME, 'label')
        for label in labels:
            self.assertIn(label.text, expected_labels, 'Lista incorecta')

        # self.assertIn(labels[0].text, expected_labels, 'Lista incorecta')
        # self.assertIn(labels[1].text, expected_labels, 'Lista incorecta')

    # Test 10
    # - Completează cu user și pass valide
    # - Click login
    # - Verifică ca noul url CONTINE /secure
    # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    # - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    # @unittest.skip
    def test_secure(self):
        print(f'Am inceput testul {self._testMethodName}')
        text = "secure area!"
        expected_url = "https://the-internet.herokuapp.com/login"

        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        WebDriverWait(self.driver, 1)
        self.driver.find_element(By.CSS_SELECTOR, 'button.radius[type="submit"]').click()
        self.driver.implicitly_wait(1)
        actual_url = self.driver.current_url
        self.assertIn('/secure', actual_url, "Textul '/secure' nu se afla in url")

        wait = WebDriverWait(self.driver, 2)
        mesaj_succes = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'flash.success')))

        # self.assertIn(text, mesaj_succes.text, "Textul cautat nu se afla in mesajul afisat. ")
        self.assertTrue(text in mesaj_succes.text, "Textul cautat nu se afla in mesajul afisat. ")

    # Test 11
    # - Completează cu user și pass valide
    # - Click login
    # - Click logout
    # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    # @unittest.skip
    def test_login(self):
        print(f'Am inceput testul {self._testMethodName}')
        expected_url = "https://the-internet.herokuapp.com/login"

        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        WebDriverWait(self.driver, 1)
        self.driver.find_element(By.CSS_SELECTOR, 'button.radius[type="submit"]').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, 'a.button.secondary.radius[href="/logout"]').click()
        self.driver.implicitly_wait(1)

        actual_url = self.driver.current_url

        self.assertEqual(expected_url, actual_url, "Invalid URL")

    # Test 12 - brute force password hacking
    # - Completează user tomsmith
    # - Găsește elementul //h4
    # - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
    # potențială parolă.
    # - Folosește o structură iterativă prin care să introduci rând pe rând
    # parolele și să apeși pe login.
    # - La final testul trebuie să îmi printeze fie
    # ‘Nu am reușit să găsesc parola’
    # ‘Parola secretă este [parola]’
    # @unittest.skip
    def test_password_hacking(self):
        print(f'Am inceput testul {self._testMethodName}')

        lista_parole = self.driver.find_element(By.CSS_SELECTOR, 'h4.subheader').text.split(" ")

        for parola in lista_parole:
            self.login('tomsmith', parola)
            if len(self.driver.find_elements(*self.LOGIN_ERROR)) > 0:
                print(f'Parola nu este buna.')
            else:
                print(f'Parola secreta este {parola}.')
                break

        actual_url = self.driver.current_url
        self.assertIn('/secure', actual_url, "Textul '/secure' nu se afla in url")
