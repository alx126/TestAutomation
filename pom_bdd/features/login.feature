Feature: Test the functionality of the Login Page

  """
  - Background este o modalitate prin care putem sa dam un context general testelor noastre
  - Functioneaza numai cu GIVEN
  - Putem sa punem in background orice context care e valabil pentru toate scenariile din feature
  """


  """
  - Daca vrem sa separam testele in categorii putem sa ne folosim de conceptul de tag-uri
  - Tag-urile incep cu semnul @ si sunt urmate de un text (recomandat sa fie ceva sugestiv pentru scenariul in scop)
  - Un scenariu poate sa fie identificat de mai multe tag-uri
  - In momentul rularii putem specifica tag-ul care ne intereseaza si se vor rula doar testele identificate de acel tag

  Exemple de comenzi pentru a rula teste cu tag-uri:
  behave --tags=smoke
  behave -f html -o behave-report.html --tags=smoke
  behave --tags=smoke,simple  [FARA SPATIU INTRE TAG-URI IN ACEST CAZ!]
  """

  Background: I am on the Login Page
    Given I am on the Login Page

  @simple @smoke
  #Scenariu1 fara parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    When I insert an unregistered email in the email input
    When I insert a password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found" message

  @parameterized @smoke
  #Scenariu1 cu parametru
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    When I insert "wrong_email@host.com" in the email input
    When I insert "parolaoarecare" in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error text contains "No customer account found"

  @parameterized @regression
  Scenario: Check that "Please enter your email" message is displayed when the user enters empty email address
    When I insert " " in the email input
    When I click on the login button
    Then Email error message is displayed
    Then Email error message text is "Please enter your email"

  @parameterized @regression
  Scenario: Check that "Wrong email" message is displayed when the user enters an email address with an invalid format
    When I insert "emailinvalid" in the email input
    When I click on the login button
    Then Email error message is displayed
    Then Email error message text is "Wrong email"

  @simple @regression
  Scenario: Check that the url is correct
    Then Login page URL is "https://demo.nopcommerce.com/login"