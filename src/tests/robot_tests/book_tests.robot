*** Settings ***
Resource  resources/resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Teardown Suite

*** Test Cases ***
Add Book With Correct Information and View It
    Go To Add Reference Page
    Set Reference Type  book
    Set Key  book key
    Set Author  Tester
    Set Title  Book Test
    Set Year  2000
    Set Publisher  testpublisher
    Set Address  Teststreet 10
    Submit Reference
    Add Reference Should Succeed With Title  Book Test

Add Book With Missing Field
    Go To Add Reference Page
    Set Reference Type  book
    Set Key  book key2
    Set Title  Book Test2
    Set Year  2001
    Set Publisher  testpublisher
    Set Address  Teststreet 10
    Submit Reference
    Add Reference Should Fail For Missing Field  Author

Add Book With Incorrect Year
    Go To Add Reference Page
    Set Reference Type  book
    Set Key  book key3
    Set Author  Tester
    Set Title  Book Test3
    Set Year  19987
    Set Publisher  testpublisher
    Set Address  Teststreet 10
    Submit Reference
    Add Reference Should Fail For Field With Message  year  Please enter a valid year.

Add Book And Delete It
    Go To Add Reference Page
    Set Reference Type  book
    Set Key  test book key
    Set Author  Tester
    Set Title  Book Test
    Set Year  2024
    Set Publisher  testpublisher
    Set Address  Teststreet 10
    Submit Reference
    Add Reference Should Succeed With Title  Book Test
    Delete Test Reference
    View Removal Verfication Page Should Be Open
    Verify Test Delete
    Delete Reference Should Succeed