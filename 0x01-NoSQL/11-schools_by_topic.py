#!/usr/bin/env python3
"""Search by topic"""
def schools_by_topic(mongo_collection, topic):
    """Returns list of schools with topic"""
    return list(mongo_collection.find({ "topics": topic }))
