*** Settings ***
Library    citation_app_library.CitationAppLibrary

*** Variables ***
${author1_form}   @article{key1,\n\tauthor = "author1"\n}
${author2_form}    @book{key2,\n\tauthor = "author2"\n}

*** Test Cases ***
App Works
    Init Default Database
    Add Input    3
    Add Input    ${EMPTY}
    Add Input    q
    Create App
    Is In Output    ${author1_form} 
    Is In Output    ${author2_form}
   