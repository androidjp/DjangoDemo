import pymongo


class PyMongoConnectionUtil:
    @staticmethod
    def getDBConnection():
        mongo_client = pymongo.MongoClient('localhost', 27017)
        db = mongo_client['notebookDB']
        return db


