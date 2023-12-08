*** Settings ***
Library  RPA.Browser.Selenium
Library  OperatingSystem
Suite Setup  Setup Suite
Suite Teardown  Teardown Suite

*** Variables ***
${DOWNLOAD_DIR}  ./tests/robot_tests/test_downloads
${FILE_NAME}  bib-file.bib

*** Test Cases ***
Download Reference File
    Go To View Reference Page
    Click Link  /view_reference/download
    Wait Until Keyword Succeeds  5 seconds  3 seconds  File Should Exist  ${DOWNLOAD_DIR}/${FILE_NAME}

*** Keywords ***
Setup Suite
    Set Download Directory  ${DOWNLOAD_DIR}
    Open Available Browser  headless=True
    Register And Login
    Add Test Category
Teardown Suite
    Close Browser
    Remove Files  ${DOWNLOAD_DIR}/*

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


Go To Register Page
    Go To  http://127.0.0.1:8000/register

Go To Login Page
    Go To  http://127.0.0.1:8000/login

Go To Category Page
    Go To  http://127.0.0.1:8000/add_category

Go To View Reference Page
    Go To  http://127.0.0.1:8000/view_reference

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
    Input Text  category  ${category}