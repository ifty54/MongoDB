# MongoDB with Python- Querying JSON Documents
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']

information = mydb.employeeinfo

record = {
    "firstName": "Christiano",
    "lastName": "Ronaldo",
    "role": "Striker"
}

records = [{
    "firstName": "Manuel",
    "lastName": "Neuer",
    "role": "Goalkeeper"
},{
    "firstName": "Sergio",
    "lastName": "Ramos",
    "role": "Defender"
},{
    "firstName": "Bruno",
    "lastName": "Fernandes",
    "role": "Attacking Midfielder"
},{
    "firstName": "Julian",
    "lastName": "Alvarez",
    "role": "Striker"
}]

goals = [{
    "league": "PL",
    "goals" : 300
},{
    "league": "League 1",
    "goals" : 260
},{
    "league": "LaLiga",
    "goals" : 290
}]

information.insert_one(record)
information.insert_many(records)
information.insert_many(goals)

#Simple way of Querying
information.find_one()

#SELECT * FROM DB
information.find()

#Also, you may write
for record in information.find({}):
    print(record)

#SELECT particular info
for records in information.find({"firstName":"Julian"}):
    print(f"Find particular item is {records}")

#Usage of $in (include), $lt (lesser than), $gt (greater than)
for records in information.find({'role':{'$in':['Striker','Goalkeeper']}}):
    print(f"Usage of $in is {records}")


for goals in information.find({'goals':{'$gt':270}}):
    print(goals)

for goals in information.find({'goals':{'$lt':280}}):
    print(goals)

#OR operators
for goals in information.find({'$or':[{'league':'LaLiga'},{'goals':300}]}):
    print(f"Stats are {goals}")

#Nested Documents
inventory = mydb.inventory
inventory.insert_many([
    {'player':'Ben White', 'size':{'h':29,'w':65}},
    {'player':'Harry Maguire', 'size':{'h':32,'w':72}}
])

for i in inventory.find({'size':{'h':29,'w':65}}):
    print(i)
