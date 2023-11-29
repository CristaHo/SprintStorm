*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Add Reference With Correct Information
    Go To Add Reference Page
    Set Author  Tester
    Set Title  The Test
    Set Year  asd
    Submit Reference
    Add Reference Should Succeed


*** Keywords ***
Add Reference Should Succeed
    View Reference Page Should Be Open
    Page Should Contain  Tester

Submit Reference
    Click Button  Add reference

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}