*** Settings ***
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

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password1
    [Arguments]  ${password1}
    Input Text  password1  ${password1}

Set Password2
    [Arguments]  ${password2}
    Input Text  password2  ${password2}

Submit Register
    Click Button  Register

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Submit Login
    Click Button  Login