from citation import Citation
from database import DatabaseHandler
from citation_app import CitationApp

if __name__ == "__main__":
    citation1 = Citation("article", "key1", {"author": "author", "title": "title"})
    db = DatabaseHandler()
    db.add(citation1)
    app = CitationApp(db)
    app.run()
