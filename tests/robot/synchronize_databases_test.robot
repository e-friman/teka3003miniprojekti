*** Settings ***
Documentation    Käyttäjänä voin synkronoida eri koneilla tallennetut viitteet.
...              Hyväksymiskriteerit:
...              - Alussa oletustietokanta ja resources/test.db sisältävät molemmat kaksi viitettä
...                samoilla avaimilla, mutta toisen tietokannan (test.db) ensimmäinen viite on uudempi
...              - Sitten synkronointi ajetaan niin, että resources/test.db synkronoidaan oletustietokantaan.
...              - Lopussa synkronoinnin jälkeen oletustietokannan ensimmäinen viite vastaa test.db:n viitettä,
...                ja toinen viite pysyy ennallaan.
Library    citation_app_library.CitationAppLibrary

*** Keywords ***
Lisaa oletussitaatit tietokantaan
    Init Default Database

Synkronoi tietokannat
    [Arguments]    ${tietokanta}
    Add input    6
    Add input    ${tietokanta}

Tulosta viitteet
    Add Input    2

Aja ohjelma
    Add Input    q
    Create App

Tarkista tuloste
    [Arguments]    ${odotettu}    ${ei_odotettu}
    Is In Output    ${odotettu}
    Is Not In Output    ${ei_odotettu}

*** Test Cases ***
Kayttajana voin synkronoida tallennetut viitteet
    Lisaa oletussitaatit tietokantaan
    Synkronoi tietokannat    resources/test.db
    Tulosta viitteet
    Aja ohjelma
    Tarkista tuloste    test_db_author1    test_db_author2