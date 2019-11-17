from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

db = GraphDatabase("http://127.0.0.1:7474/db/data/")
q = 'MATCH (u:User)-[r:likes]->(m:Beer) ' \
    'WHERE u.name="Marco" ' \
    'RETURN u, type(r), m'
#what the query is trying to match is “any node n, linked to a node m via a relationship r“.

results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))