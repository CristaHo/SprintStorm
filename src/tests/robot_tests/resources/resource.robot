*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Resource  reference_resource.robot
Resource  download_resource.robot
Resource  user_resource.robot


*** Variables ***
${SERVER}  localhost:8000
${DELAY}  0 seconds
${FRONTPAGE_URL}  http://${SERVER}
${ADD_REFERENCE_URL}  http://${SERVER}/add_reference
${VIEW_REFERENCE_URL}  http://${SERVER}/view_reference
${REGISTER_URL}  http://${SERVER}/register
${LOGIN_URL}  http://${SERVER}/login
${CATEGORY_URL}  http://${SERVER}/add_category
${DELETE_USER_URL}  http://${SERVER}/delete_user

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}
    Register
    Login

Teardown Suite
    Delete User
    Close Browser

Front Page Should Be Open
    Title Should Be  Bibtex maker - Frontpage

Add Reference Page Should Be Open
    Title Should Be  Bibtex maker - Add reference

View Reference Page Should Be Open
    Title Should Be  Bibtex maker - View references

View Removal Verfication Page Should Be Open
    Title Should Be  Bibtex maker - Verify removal

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

Delete User
    Go To  ${DELETE_USER_URL}

Set Category
    [Arguments]  ${category}
    Input Text  name  ${category}

Add Test Category
    Go To Category Page
    Set Category  testcategory
    Click Button  Add category

Delete Test Category
    Click Button  Delete

Delete Test Reference
    Click Button  Delete this reference

Verify Test Delete
    Click Button  name:submit