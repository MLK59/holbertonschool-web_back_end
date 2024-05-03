#!/usr/bin/env python3
""" function that inserts a new document in a collection
based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Insert the document into the collection"""
    p = mongo_collection.insert_one(kwargs)
    return p.inserted_id
