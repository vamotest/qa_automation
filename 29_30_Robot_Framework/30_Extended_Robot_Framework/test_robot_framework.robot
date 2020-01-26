*** Settings ***
Documentation      Suite description
Library            Selenium2Library
Resource           opencart.robot
Test Setup         Open Opencart Login Page
Test Teardown      Close browser


*** Variables ***
${USER}             user
${PASSWORD}         bitnami1
${NEW_PRODUCT}      iPhone 11 Pro Max 64 GB
${NEW_TAG}          iOS 13
${NEW_MODEL}        A2215


*** Test Cases ***
Admin login -> open catalog -> open products -> admin logout
    Authenticate                 ${USER}    ${PASSWORD}
    Maximize Browser Window
    Open catalog
    Open products
    Click logout
    Close browser


Add new product
    Authenticate                 ${USER}    ${PASSWORD}
    Maximize Browser Window
    Open catalog
    Open products
    Click add new button
    Add new product              ${NEW_PRODUCT}
    Add new tag                  ${NEW_TAG}
    Click navigation data
    Add new model                ${NEW_MODEL}
    Click save button
    Close browser


Delete product
    Authenticate                 ${USER}    ${PASSWORD}
    Maximize Browser Window
    Open catalog
    Open products
    Click product to delete
    Click delete button
    Handle Alert
    Close browser
