#!/usr/bin/env python3
"""using pyMongo"""


def update_topics(mongo_collection, name, topics):
    """a function changes all topics of a school document based on the name"""
    old_documents = {"name": name}
    new_documents = {"$set": {"topics": topics}}
    mongo_collection.update_many(old_documents, new_documents)
