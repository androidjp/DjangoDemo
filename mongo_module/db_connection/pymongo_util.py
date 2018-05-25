import threading

import pymongo


# 单例
class PyMongoConnection:
    _instance_lock = threading.Lock()
    dbConnection = None

    def __init__(self):
        print("连接MongoDB")
        self.dbConnection = pymongo.MongoClient('localhost', 27017)
        print("连接完毕")

    def __new__(cls, *args, **kwargs):
        if not hasattr(PyMongoConnection, "_instance"):
            with PyMongoConnection._instance_lock:
                if not hasattr(PyMongoConnection, "_instance"):
                    PyMongoConnection._instance = object.__new__(cls)
        return PyMongoConnection._instance

    def getDBCollection(self, dbName, collectionName):
        return (self.dbConnection[dbName])[collectionName]

pyMongoConnection = PyMongoConnection()
