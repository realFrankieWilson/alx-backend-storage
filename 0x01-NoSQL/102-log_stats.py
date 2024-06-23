#!/usr/bin/env python3
from pymongo import MongoClient
from collections import Counter

# MongoDB connection details
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "logs"
MONGO_COLLECTION = "nginx"

# Connect to MongoDB
client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Get the total number of documents
total_docs = collection.count_documents({})
print(f"{total_docs} logs")

print("Methods:")

# Get the count of documents for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Get the count of documents with method=GET and path=/status
count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{count} status check")

# Get the top 10 most frequent IPs
ip_counts = Counter(collection.distinct("ip"))
top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print("IPs:")
for ip, count in top_ips:
    print(f"\t{ip}: {count}")

# Close the MongoDB connection
client.close()
