#!/usr/bin/env python3
"""Provides stats about Nginx logs"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

print(f"{collection.count_documents({})} logs")
print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_count} status check")
