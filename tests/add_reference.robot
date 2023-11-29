*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Add Book With Correct Information
    Go To Add Reference Page
    Choose Reference Type  book
    Set Key  book key
    Set Author  Tester
    Set Title  Book Test
    Set Year  2000
    Set Publisher  testpublisher
    Submit Reference
    Add Reference Should Succeed  Book Test

Add Article With Correct Information
    Go To Add Reference Page
    Choose Reference Type  article
    Set Key  article key
    Set Author  Tester
    Set Title  Article Test
    Set Year  2000
    Set Journal  test journal
    Set Volume  12
    Set Pages  100-200
    Submit Reference
    Add Reference Should Succeed  Article Test


*** Keywords ***
Add Reference Should Succeed
    View Reference Page Should Be Open
    [Arguments]  ${title}
    Page Should Contain  ${title}

Choose Reference Type
    [Arguments]  ${type}
    Select From List by Value  id=ref  ${type}
    Click Button  Select

Submit Reference
    Click Button  Add reference

Set Key
    [Arguments]  ${key}
    Input Text  key  ${key}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}