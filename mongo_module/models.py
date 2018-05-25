# encoding=utf-8
import re
from .db_connection.db_connection_utils import PyMongoConnectionUtil

pattern = re.compile(r'^_[\w,\d]*$')


class PyMongoModel():
    def __init__(self, collectionObj) -> None:
        self.collectionObj = collectionObj

    def add(self, jsonStr):
        self.collectionObj.insert(jsonStr)

    def remove(self, id):
        pass

    def update(self, jsonStr):
        pass

    def findAll(self):
        cursor = self.collectionObj.find()
        resultArr = []
        # item's type is dict
        for item in cursor:
            # resDict = dict(map(lambda key,value: pattern.match(key) is not None, item))
            res = item.copy()
            for key in item:
                if pattern.match(key) is not None:
                    del res[key]
            item.clear()
            resultArr.append(res)
        return resultArr


class UserModel(PyMongoModel):
    def __init__(self):
        super().__init__(PyMongoConnectionUtil.getDBConnection().USER)


class NoteModel(PyMongoModel):
    def __init__(self):
        super().__init__(PyMongoConnectionUtil.getDBConnection().NOTE)
