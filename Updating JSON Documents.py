# MongoDB with Python- Updating JSON Documents
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client["education"]
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

versity.update_one(
  {
    "dept": "Math",
     "student": 80,
     "section": {"a": 20, "b": 50, "c": 10},
     "head": "Matilda"
  }
)

