*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Resource  reference_resource.robot

*** Variables ***
${DOWNLOAD_DIR}  ./tests/robot_tests/test_downloads
${FILE_NAME}  bib-file.bib

*** Keywords ***
Download Setup Suite
    ${absolute_path}=  Evaluate  os.path.abspath('${DOWNLOAD_DIR}')  os
    ${prefs}=  Create Dictionary  download.default_directory  ${absolute_path}
    ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_experimental_option  prefs  ${prefs}
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  0 second
    Register
    Login
    Add Test Category
Teardown Suite
    Close Browser
    Remove Files  ${DOWNLOAD_DIR}/*

Add Book Reference
    Go To Add Reference Page
    Choose Reference Type  book
    Set Key  book key2
    Set Author  Tester
    Set Title  Book Test
    Set Year  2000
    Set Publisher  testpublisher
    Set Address  Teststreet 10
    Submit Reference

    