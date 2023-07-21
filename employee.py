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
information.insert_one(record)
information.insert_many(records)

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
