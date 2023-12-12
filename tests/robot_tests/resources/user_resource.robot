*** Settings ***
Library  SeleniumLibrary
Resource  resource.robot

*** Keywords ***
Register
    Go To Register Page
    Set Username  test
    Set Password1  1234
    Set Password2  1234
    Submit Register

Login
    Go To Login Page
    Set Username  test
    Set Password  1234
    Submit Login