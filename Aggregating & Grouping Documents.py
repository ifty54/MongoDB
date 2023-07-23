import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client["Employee"]
collection = mydb["Scores"]

data = [{"name": "Alan", "subject": "MTE", "score": 90},
        {"name": "George", "subject": "CSE", "score": 70},
        {"name": "Donald", "subject": "CEE", "score": 80},
        {"name": "Alan", "subject": "EEE", "score": 20},
        {"name": "George", "subject": "EEE", "score": 30},
        {"name": "Donald", "subject": "EEE", "score": 50}]

collection.insert_many(data)

#Aggregate method

aggregation = collection.aggregate(
  [{"$group" : {"_id":"$name", "Total Marks": {"$sum":"$score"}}}]
)
for i in aggregation:
  print(i)

#Aggregate method Adding Marks

aggregation = collection.aggregate(
  [{"$group" : {"_id":"$name", "Total Subject": {"$sum":1}}}]
)
for i in aggregation:
  print(i)

