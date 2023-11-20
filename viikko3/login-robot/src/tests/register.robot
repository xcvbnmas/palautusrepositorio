*** Settings ***
Resource  resource.robot
Library  ../AppLibrary.py

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Create User  kalle  kalle123

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Create User  kalle  kalle123

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Run Keyword And Expect Error  Should Raise Error  Invalid username

Register With Enough Long But Invalid Username And Valid Password
#

Register With Valid Username And Too Short Password
#

Register With Valid Username And Long Enough Password Containing Only Letters
#

*** Keywords ***
Input Register Command
    Create User

Input Valid Registration Credentials
    Input Credentials  kalle  kalle123
    Input Register Command
    
Should Raise Error
    [Arguments]  ${expected_error}  ${block}
    Run Keyword And Expect Error  ${expected_error}  ${block}
