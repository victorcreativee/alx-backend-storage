#!/usr/bin/env python3
"""Insert a new document"""
def insert_school(mongo_collection, **kwargs):
    """Inserts document and returns the _id"""
    return mongo_collection.insert_one(kwargs).inserted_id
