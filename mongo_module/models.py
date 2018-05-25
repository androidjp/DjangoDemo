# User pymongo
import pymongo

# 1. 建立连接，获取客户端对象
mongo_client = pymongo.MongoClient('localhost', 27017)
# 2. 获取数据库对象
db = mongo_client.notebookDB

# 3. 获取集合对象
collection_note = db.note
collection_user = db.user


class PyMongoModel():

    def add(self, jsonStr):
        pass

    def remove(self, id):
        pass

    def update(self, jsonStr):
        pass

    def find(self, id):
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
