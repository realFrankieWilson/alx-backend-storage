#!/usr/bin/env python3
"""
Module `12-log_stats`
A script that provides some stats about
Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


# Connection details
MONGO_DB = "logs"
MONGO_PORT = 27017
MONGO_HOST = "localhost"
MONGO_COLLECTION = "nginx"

# making connection to the database.
client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Gets the total number of documents
total_num_of_doc = collection.count_documents({})
print(f"{total_num_of_doc} logs")

print("Methods:")

# Counts the document for each HTTP mehtod
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
status_checked = 0
for methd in methods:
    count = collection.count_documents({"method": methd})

    status_checked += 1

    if methd == "GET":
        print(f"\tmethod GET: {count}")
    elif methd == "POST":
        print(f"\tmethod POST: {count}")
    elif methd == "PUT":
        print(f"\tmethod PUT: {count}")
    elif methd == "PATCH":
        print(f"\tmethod PATCH: {count}")
    else:
        print(f"\tmethod DELETE: {count}")


# Counts documents with the GET method and path=/status
count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{count} status check")

# Close connection to MongoDB
client.close()
