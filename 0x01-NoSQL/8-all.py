#!/usr/bin/env python3
"""List all documents in collection"""
def list_all(mongo_collection):
    """Returns all documents in a collection"""
    return list(mongo_collection.find()) if mongo_collection else []
