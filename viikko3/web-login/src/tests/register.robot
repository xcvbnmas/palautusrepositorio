*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle456
    Submit Registration
    Registration Should Succeed
    
Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle456
    Submit Registration
    Registration Should Fail With Message  Username is too short
    
*** Keywords ***

Go To Register Page
    Go To  ${REGISTER_URL}
    Register Page Should Be Open
    
Submit Registration
    Click Button  Register

Registration Should Succeed
    Go To  ${HOME_URL}
    
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    
Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
