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
