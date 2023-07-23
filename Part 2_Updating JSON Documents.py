# MongoDB with Python- Updating JSON Documents
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client["Employee"]
versity = mydb.versity

versity.insert_many([{"dept": "EEE",
     "student": 100,
     "section": {"a": 35, "b": 35, "c": 30},
     "head": "John"},
{"dept": "ME",
     "student": 60,
     "section": {"a": 20, "b": 20, "c": 20},
     "head": "Laura"},
{"dept": "CSE",
     "student": 120,
     "section": {"a": 30, "b": 40, "c": 50},
     "head": "Andy"}])

#Update_one function basically changes or modifies any data from one specific dictionary element. 
#Here, I change values of dept: CSE

#1
versity.update_one(
  {"dept": "CSE"},
     {"$set": {"section.b": 100}, "$CurrentDate": {"LastModified":True}}
)

#2
versity.update_one(
{"dept":"ME"},
{"$set":{"student":200},
"$currentDate":{"lastModified":True}}
)

#Update_many() lets you build more than one logic at a time

versity.update_many(
    {"student": {"$lt": 100}},
    {"$set": {"section.b": 10, "section.c": 10},
     "$currentDate": {"lastModified": True}})

#Replace function can replace the whole item of the dictionary according to your newest elements

versity.replace_one(
     {"dept":"CSE"},
          {"dept":"CSE","section":{"a": 4, "b": 6}}
)
