#!/usr/bin/env python3
""" Log stats with top 10 IPs """
from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({ "method": method })
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({ "method": "GET", "path": "/status" })
    print(f"{status_check} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    for ip_doc in collection.aggregate(pipeline):
        print(f"\t{ip_doc['_id']}: {ip_doc['count']}")

if __name__ == "__main__":
    log_stats()
