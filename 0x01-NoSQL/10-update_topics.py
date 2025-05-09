#!/usr/bin/env python3
"""Update topics"""
def update_topics(mongo_collection, name, topics):
    """Update topics for a school"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
