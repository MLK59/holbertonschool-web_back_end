#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """ return list of collection mongo"""
    T = mongo_collection.find()
    return T if T else []
