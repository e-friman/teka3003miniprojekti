*** Settings ***
Documentation    Käyttäjänä voin lisätä viitteisiin kategorioita tai tägejä,
...              jotta voin tehdä tarkempia hakuja.
...
...              Hyväksymiskriteerit:
...              - Alussa järjestelmässä on vähintään yksi tallennettu viite
...                ilman kategorioita tai tägejä.
...              - Sitten käyttäjä lisää viitteelle yhden tai useamman
...                kategorian tai tägin ja tallentaa muutokset.
...              - Lopussa viite sisältää lisätyt tägit ja
...                haku palauttaa viitteen, kun haku suoritetaan kyseisellä
...                tägillä.

Library    citation_app_library.CitationAppLibrary

*** Keywords ***
Lisaa oletussitaatit tietokantaan
    Init Default Database

Lisaa viite tietokantaan
    [Arguments]    ${tag}
    Add Input    1
    Add Input    book
    Add Input    key3
    Add Input    author3
    Add Input    title3
    Add Input    publisher3
    Add Input    2025
    Add Input    ${tag}


Hae viitteet tagin perusteella
    [Arguments]    ${tag}
    Add Input    3
    Add Input    tag
    Add Input    ${tag}
    Add Input    ${EMPTY}

Aja ohjelma
    Add Input    q
    Create App

Tarkista tuloste
    [Arguments]    ${odotettu}    ${ei_odotettu}      ${ei_odotettu2}
    Is In Output    ${odotettu}
    Is Not In Output    ${ei_odotettu}
    Is Not In Output    ${ei_odotettu2}

*** Test Cases ***
Kayttajan voin lisata tageja viitteisiin ja hakea niilla
    Lisaa oletussitaatit tietokantaan
    Lisaa viite tietokantaan     minun_tag
    Hae viitteet tagin perusteella    minun_tag
    Aja ohjelma
    Tarkista tuloste    author3    author1    author2
