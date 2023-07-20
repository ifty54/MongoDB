import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']

information = mydb.employeeinfo

record = {
    "firstName": "Christiano",
    "lastName": "Ronaldo",
    "role": "Striker"
}
information.insert_one(record)