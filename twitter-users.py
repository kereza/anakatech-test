#! /usr/bin/python
import pprint
from pymongo import MongoClient

listA = []

client = MongoClient('172.31.0.156', 32773)

db = client['anakatech']
coll = db['twitterMessagesDocker']


many_docs = coll.find()
for doc in many_docs:
        print(doc['username'])
