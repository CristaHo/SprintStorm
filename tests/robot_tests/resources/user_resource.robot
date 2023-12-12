*** Settings ***
Library  SeleniumLibrary
Resource  resource.robot

*** Keywords ***
User Setup Suite
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    #Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Register
    Go To Register Page
    Set Username  test
    Set Password1  1234
    Set Password2  1234
    Submit Register

Login
    Go To Login Page
    Set Username  test
    Set Password  1234
    Submit Login