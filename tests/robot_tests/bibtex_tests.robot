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
    Open Available Browser  http://127.0.0.1:8000/view_reference  headless=True
    Click Link  /view_reference/download
    Wait Until Keyword Succeeds  5 seconds  3 seconds  File Should Exist  ${DOWNLOAD_DIR}/${FILE_NAME}

*** Keywords ***
Setup Suite
    Set Download Directory  ${DOWNLOAD_DIR}
Teardown Suite
    Close Browser
    Remove Files  ${DOWNLOAD_DIR}/*