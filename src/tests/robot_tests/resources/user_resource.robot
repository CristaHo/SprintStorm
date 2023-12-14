*** Settings ***
Resource  resource.robot

*** Keywords ***
User Setup Suite
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Register
    Go To Register Page
    Set Username  robot_test
    Set Password1  12345678
    Set Password2  12345678
    Submit Register

Login
    Go To Login Page
    Set Username  robot_test
    Set Password  12345678
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

logout
    Go To Front Page
    Click Link  /logout