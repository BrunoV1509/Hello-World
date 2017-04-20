import pymongo
import pprint

from pymongo import MongoClient

uri="mongodb://username:password@/admin?authMechanism=SCRAM-SHA-1&replicaSet=UAT02_SPT_RS1"

client=MongoClient(uri)

db=client.admin

collection=db.system.users

pprint.pprint( collection.find_one())


