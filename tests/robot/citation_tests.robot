*** Settings ***
Library    app_library.AppLibrary

*** Test Cases ***
Citation Initialization Works
    ${c}=    Create Citation    article    a1    {"author": "Bob"}
    Should Be Equal    ${c.type}    article
    Should Be Equal    ${c.key}    a1
    Should Be Equal    ${c.data["author"]}    Bob

Citation String Representation Works
    ${c}=    Create Citation    article    a1    {"title": "My Title"}
    ${s}=    Citation To String    ${c}
    Should Contain    ${s}    My Title

Database Starts Empty
    ${db}=    Create Database
    ${items}=    Database All    ${db}
    Length Should Be    ${items}    0

Database Adding Items Works
    ${db}=       Create Database
    ${c}=        Create Citation    article    k1    {"author": "A"}
    Database Add    ${db}    ${c}
    ${items}=    Database All    ${db}
    Length Should Be    ${items}    1

Lomake Produces Citation
    ${values}=    Create List    article    key1    Bob    My Title    My Journal    2025
    ${result}=    Create Lomake Citation    ${values}
    Should Be Equal    ${result.type}    article
    Should Be Equal    ${result.key}     key1
    Should Be Equal    ${result.data["author"]}    Bob
    Should Be Equal    ${result.data["title"]}     My Title
    Should Be Equal    ${result.data["journal"]}   My Journal
    Should Be Equal    ${result.data["year"]}      2025
