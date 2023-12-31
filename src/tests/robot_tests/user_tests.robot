*** Settings ***
Resource  resources/resource.robot
Suite Setup  User Setup Suite
Suite Teardown  Teardown Suite

*** Test Cases ***
Create Account Login And View References
    Register
    Front Page Should Be Open
    Page Should Contain  User created
    Login
    Front Page Should Be Open
    Page Should Contain Link  /logout
    Add Book Reference
    Add Reference Should Succeed With Title  Book Test
    Go To View Reference Page
    Page Should Contain  Book Test
    Logout

Login And Create Reference With Category
    Login
    Front Page Should Be Open
    Page Should Contain Link  /logout
    Add Test Category
    Add Book With Category
    Add Reference Should Succeed With Title  Book Test
    Go To View Reference Page
    Page Should Contain  Book Test
    Logout

Login And View Reference By Category
    Login
    Front Page Should Be Open
    Page Should Contain Link  /logout
    Go To View Reference Page
    Select Category  testcategory
    Submit Filter
    Page Should Contain  Book Test
    Logout