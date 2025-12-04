*** Settings ***
Library    citation_app_library.CitationAppLibrary

*** Test Cases ***
App Works
    Init Default Database
    Add Input    4
    Add Input    author
    Add Input    author1
    Add Input    ${EMPTY}
    Add Input    q
    Create App
    Is In Output    author1
    Is Not In Output    author2