# encoding=utf-8
import re

from ..db_connection.pymongo_util import pyMongoConnection

pattern = re.compile(r'^_[\w,\d]*$')


class PyMongoDAO:
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
        for item in cursor:
            res = self.filterUselessFields(item)
            resultArr.append(res)
        return resultArr

    def filterUselessFields(self, item):
        if item is None:
            return None
        res = item.copy()
        for key in item:
            if pattern.match(key) is not None:
                del res[key]
        item.clear()
        return res


class UserDAO(PyMongoDAO):
    def __init__(self):
        super().__init__(pyMongoConnection.getDBCollection("notebookDB", "USER"))

    def findUserByPhoneNumOrEmail(self, userId):
        resUser = self.collectionObj.find_one({"$or": [{"PHONE_NUMBER": userId}, {"EMAIL_ADDRESS": userId}]})
        return self.filterUselessFields(resUser)


class NoteDAO(PyMongoDAO):
    def __init__(self):
        super().__init__(pyMongoConnection.getDBCollection("notebookDB", "NOTE"))
