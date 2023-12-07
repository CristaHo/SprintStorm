*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:8000
${DELAY}  0 seconds
${FRONTPAGE_URL}  http://${SERVER}
${ADD_REFERENCE_URL}  http://${SERVER}/add_reference
${VIEW_REFERENCE_URL}  http://${SERVER}/view_reference
${REGISTER_URL}  http://${SERVER}/register
${LOGIN_URL}  http://${SERVER}/login

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

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