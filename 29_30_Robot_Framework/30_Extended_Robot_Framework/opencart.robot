*** Variables ***
${URL}                      http://localhost/admin
${BROWSER}                  chrome
${USERNAME_FIELD}           id:input-username
${PASSWORD_FIELD}           id:input-password
${LOGIN_BUTTUN}             css:button[type='submit']
${CATALOG}                  css:li[id='menu-catalog']
${PRODUCTS}                 xpath=*//a[text()='Products']
${LOGOUT_BUTTUN}            xpath=//*[@id="header"]/div/ul/li[2]/a/span
${ADD_NEW_BUTTON}           xpath=//*[@id="content"]/div[1]/div/div/a/i
${PRODUCT_NAME_FIELD}       xpath=//*[@id="input-name1"]
${META_TAG_TITLE_FIELD}     xpath=//*[@id="input-meta-title1"]
${NAVIGATION_DATA}          xpath=//*[@id="form-product"]/ul/li[2]/a
${MODEL_FIELD}              xpath=//*[@id="input-model"]
${SAVE_BUTTON}              xpath=//*[@id="content"]/div[1]/div/div/button
${PRODUCT_TO_DELETE}        xpath=//*[@id="form-product"]/div/table/tbody/tr[1]/td[1]/input
${DELETE_BUTTON}            xpath=//*[@id="content"]/div[1]/div/div/button[3]


*** Keywords ***
Open Opencart Login Page
    Open Browser                        ${URL}    browser=${BROWSER}

Input username
    [Arguments]                        ${USERNAME}
    Input text                          ${USERNAME_FIELD}    ${USERNAME}

Input password
    [Arguments]                        ${PASSWORD}
    Input text                          ${PASSWORD_FIELD}    ${PASSWORD}

Click login
    Click Button                        ${LOGIN_BUTTUN}

Open catalog
    Click Element                       ${CATALOG}

Open products
    Wait Until Element Is Visible       ${PRODUCTS}
    Click Element                       ${PRODUCTS}

Click logout
    Wait Until Element Is Visible       ${LOGOUT_BUTTUN}
    Click Element                       ${LOGOUT_BUTTUN}
    Wait Until Element Is Not Visible   ${LOGOUT_BUTTUN}

Click add new button
    Wait Until Element Is Visible       ${ADD_NEW_BUTTON}
    Click Element                       ${ADD_NEW_BUTTON}

Click navigation data
    Click Element                       ${NAVIGATION_DATA}

Click save button
    Click Button                        ${SAVE_BUTTON}
    Wait Until Element Is Not Visible   ${SAVE_BUTTON}

Click product to delete
    Click Element                       ${PRODUCT_TO_DELETE}

Click delete button
    Wait Until Element Is Visible       ${DELETE_BUTTON}
    Click Button                        ${DELETE_BUTTON}

Authenticate
    [Arguments]                        ${USER}    ${PASSWORD}
    Input username                      ${USER}
    Input password                      ${PASSWORD}
    Click login

Add new product
    [Arguments]                        ${NEW_PRODUCT}
    Click Element                       ${PRODUCT_NAME_FIELD}
    Input text                          ${PRODUCT_NAME_FIELD}    ${NEW_PRODUCT}

Add new tag
    [Arguments]                        ${NEW_TAG}
    Click Element                       ${META_TAG_TITLE_FIELD}
    Input text                          ${META_TAG_TITLE_FIELD}    ${NEW_TAG}

Add new model
    [Arguments]                        ${NEW_MODEL}
    Wait Until Element Is Visible       ${MODEL_FIELD}
    Click Element                       ${MODEL_FIELD}
    Input text                          ${MODEL_FIELD}    ${NEW_MODEL}

