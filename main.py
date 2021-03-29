import pymongo
from pymongo import MongoClient
from pymongo import collection

cluster = MongoClient("mongodb+srv://bouthaina:<>@cluster0.xg2ff.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post = {"_id": 0, "nam": "ayedi", "score": 79}
collection.insert_one(post)

