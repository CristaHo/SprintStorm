*** Settings ***
Resource  resource.robot

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
Download Teardown Suite
    Close Browser
    Remove Files  ${DOWNLOAD_DIR}/*

    