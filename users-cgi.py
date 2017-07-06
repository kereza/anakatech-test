#!/usr/bin/python
print("Content-Type: text/html\n")

from pymongo import MongoClient

listA = []
client = MongoClient('172.31.0.156', 32773)

db = client['anakatech']
coll = db['twitterMessagesDocker']

many_docs = coll.find()
for doc in many_docs:
    listA.append(doc['username'])

for a in (listA[-15:]):
    print(a)
    print('<br>')
