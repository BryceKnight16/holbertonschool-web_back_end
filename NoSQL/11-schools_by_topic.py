#!/usr/bin/env python3
"""
PyMongo
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    query = {"topics": topic}
    the_list = mongo_collection.find(query)
    return the_list
