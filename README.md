# MongoDB
![image](https://github.com/ifty54/MongoDB/assets/31790027/f3adedb7-dc88-4417-8049-412e82090ef3)

## Installation

Visit:

https://www.mongodb.com/try/download/community

Download the Community Edition and Boom!

The rest process of installation in your local machine is easy-to-go. Then, Install:

MongoDB Shell or mongosh

Make sure that you have add the bin sources of Mongod and Mongosh into the path of your local machine's Environmental Variables. 

![Screenshot (67)](https://github.com/ifty54/MongoDB/assets/31790027/9075fdb9-eb74-4483-9510-9a2e63b4136d)

Now, it's time to have fun! Your MongoDB is set to go!

Go to your Command Prompt! 
`use Employee` # Employee is a `db_name`

```bash
db.collection.insertOne(

{

firstname: "Al Amin",

lastname: "Ifty",

age: 26

})
```

That's how you can create a JSON file on the prompt. And it'll directly update the MongoDB server if the rest process is okay since installation.

## Pymongo Installation (Join any local or virtual Python IDE with MongoDB)
Via Terminal:

`pip install pymongo`

Via Python File: (For Ex)
```bash
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
```
