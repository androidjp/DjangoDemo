# encoding=utf-8
import re

import pymongo

# 1. 建立连接，获取客户端对象

pattern = re.compile(r'^_[\w,\d]*$')

mongo_client = pymongo.MongoClient('localhost', 27017)
# 2. 获取数据库对象
db = mongo_client.notebookDB


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
        super().__init__(db.USER)

    pass


class NoteModel(PyMongoModel):
    def __init__(self):
        super().__init__(db.note)

    pass

# class User(models.Model):
#     phone_number = models.CharField(max_length=15, primary_key=True)
#     email_address = models.CharField(max_length=30)
#     nick_name = models.CharField(max_length=20)
#     password = models.CharField(max_length=16)
#     create_time = models.DateTimeField('user create date')
#
#     def __str__(self):
#         return 'User : ' + self.nick_name
#
#
# class Note(models.Model):
#     title = models.CharField(max_length=40)
#     content = models.CharField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     update_date = models.DateTimeField('date update note')
#     create_date = models.DateTimeField('date create note')
#
#     def __str__(self):
#         return self.title + ":" + self.content
