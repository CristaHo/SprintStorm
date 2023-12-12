*** Settings ***
Resource  resources/resource.robot
Suite Setup  Download Setup Suite
Suite Teardown  Download Teardown Suite


*** Test Cases ***
Create reference and Download BibTeX File
    Add Book Reference
    Go To View Reference Page
    Click Link  /view_reference/download
    Wait Until Keyword Succeeds  5 seconds  1 seconds  File Should Exist  ${DOWNLOAD_DIR}/${FILE_NAME}