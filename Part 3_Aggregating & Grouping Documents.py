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
  [{"$group" : {"_id":"$name", "Total Subject": {"$sum":1}}}]
)
for i in aggregation:
  print(i)
        
#Aggregate method Adding Marks

aggregation = collection.aggregate(
  [{"$group" : {"_id":"$name", "Total Marks": {"$sum":"$score"}}}]
)
for i in aggregation:
  print(i)

#Calculating average

aggregation = collection.aggregate(
  [{"$group" : {"_id":"$name", "Average": {"$avg":"$score"}}}]
)
for i in aggregation:
  print(i)

import datetime

data = [{ "_id" : 1, "job" : "Writer", "salary" : 10000, "experience" : 2, "date" : datetime.datetime.utcnow()},
{ "_id" : 2, "job" : "Engineer", "salary" : 20000, "experience" : 1, "date" : datetime.datetime.utcnow() },
{ "_id" : 3, "job" : "Banker", "salary" : 5000, "experience" : 5, "date" : datetime.datetime.utcnow() },
{ "_id" : 4, "job" : "Doctor", "salary" : 70000, "experience" : 10, "date" : datetime.datetime.utcnow() },
{ "_id" : 5, "job" : "Scientist", "salary" : 500000, "experience" : 10, "date" :datetime.datetime.utcnow() }]

print(data)

newcollection = mydb["professional"]
newcollection.insert_many(data)

#Example

aggregation = newcollection.aggregate(
  [{"$group" : {"_id":"$job", 
                "Exp-Sal Ratio": {"$avg" : {"$multiply" : ["$salary","$experience"]}},
                "Average Salary" : {"$avg":"$salary"}}}]
)
for i in aggregation:
  print(i)
