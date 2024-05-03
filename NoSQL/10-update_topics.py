#!/usr/bin/env python3
""" a Python function that changes all topics of a school document
based on the name """


def update_topics(mongo_collection, name, topics):
    """ Update the topics of the document"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
