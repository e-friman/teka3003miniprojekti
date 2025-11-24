from Citation import Citation
from Database import MemoryDatabase
citation = Citation("article", "key1", {"author": "author", "title": "title"})


db = MemoryDatabase()
db.add(citation)

print(db.get_all())
print(str(db.get_all()[0]))
