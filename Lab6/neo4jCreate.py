from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://127.0.0.1:7474/db/data/")
#http://localhost:7474/db/data/
#
#
## Create some nodes with labels
user = db.labels.create("User")
u1= db.nodes.create(name="Marco")
user.add(u1)
u2 = db.nodes.create(name="Daniela")
user.add(u2)

beer = db.labels.create("Beer")
b1 = db.nodes.create(name="Punk IPA")
b2 = db.nodes.create(name="Hoegaarden Rosee")

## Associating a label with many nodes in one go
beer.add(b1, b2)

##Create relationships:
u1.relationships.create("likes", b1)
u1.relationships.create("likes", b2)
u2.relationships.create("likes", b1)

## Bi-directional relationships
u1.relationships.create("friends", u2)