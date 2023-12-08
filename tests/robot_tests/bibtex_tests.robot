*** Settings ***
Library  OperatingSystem
Resource  bibtex_resource.robot
Suite Setup  Setup Suite
Suite Teardown  Teardown Suite


*** Test Cases ***
Download Reference File
    Go To View Reference Page
    Click Link  /view_reference/download
    Wait Until Keyword Succeeds  5 seconds  3 seconds  File Should Exist  ${DOWNLOAD_DIR}/${FILE_NAME}

