*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${SERVER}  localhost:8000
${DELAY}  0 seconds
${FRONTPAGE_URL}  http://${SERVER}
${ADD_REFERENCE_URL}  http://${SERVER}/add_reference
${VIEW_REFERENCE_URL}  http://${SERVER}/view_reference
${REGISTER_URL}  http://${SERVER}/register
${LOGIN_URL}  http://${SERVER}/login
${CATEGORY_URL}  http://${SERVER}/add_category

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}
    Register And Login
    Add Test Category

Front Page Should Be Open
    Title Should Be  Bibtex maker - Frontpage

Add Reference Page Should Be Open
    Title Should Be  Bibtex maker - Add reference

View Reference Page Should Be Open
    Title Should Be  Bibtex maker - View references

Go To Front Page
    Go To  ${FRONTPAGE_URL}

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Go To View Reference Page
    Go To  ${VIEW_REFERENCE_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Category Page
    Go To  ${CATEGORY_URL}

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

Set Category
    [Arguments]  ${category}
    Input Text  name  ${category}

Choose Reference Type
    [Arguments]  ${type}
    Select From List by Value  id=ref  ${type}
    Click Button  Select

Register And Login
    Go To Register Page
    Set Username  test
    Set Password1  1234
    Set Password2  1234
    Submit Register
    Go To Login Page
    Set Username  test
    Set Password  1234
    Submit Login

Add Test Category
    Go To Category Page
    Set Category  test
    Click Button  Add category