import os
from database import DatabaseHandler
from citation_app import CitationApp

if __name__ == "__main__":
    db = DatabaseHandler()
    try:
        db.load_from_file("db/citations_db.json")
    except FileNotFoundError:
        pass
    app = CitationApp(db)
    try:
        app.run()
    except KeyboardInterrupt:
        # pitää ottaa tää kiinni, jos halutaan tallentaa tiedot vaikka
        # käyttäjä painaa ctrl+c
        # muitten poikkeuksien annetaan mennä läpi,
        # jotta vastaavasti databasea ei tallenneta, jos
        # ohjelma kaatuu jostain muusta syystä
        # esim. virheellisestä datasta
        pass
    if not os.path.exists("db"):
        os.makedirs("db")
    db.save_to_file("db/citations_db.json")
