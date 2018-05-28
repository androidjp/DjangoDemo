import datetime

from mongoengine import *

connect('notebookDB', host='localhost', port=27017)


# meta 键值说明： collection 表示我要映射到数据库的哪张表， strict 表示我是否可以忽略额外的属性
class Note(Document):
    TITLE = StringField(required=True, max_length=30)
    CONTENT = StringField(required=False)
    USER_ID = StringField(required=True, max_length=20)
    UPDATE_DATE = DateTimeField(required=True)
    CREATE_DATE = DateTimeField(required=True)
    meta = {'collection': 'NOTE', 'strict': False}

    def toJsonObj(self):
        return {
            "TITLE": self.TITLE,
            "CONTENT": self.CONTENT,
            "USER_ID": self.USER_ID,
            "UPDATE_DATE": self.UPDATE_DATE,
            "UPDATE_DATE": self.UPDATE_DATE
        }


class NoteDAO:
    def findAll(self):
        noteList = Note.objects.all()
        noteListRes = []
        for note in noteList:
            print("note-> title:", note.TITLE, " content:", note.CONTENT)
            noteListRes.append(note.toJsonObj())
        return noteListRes

    def add(self, note):
        n = Note()
        n.TITLE = note['title']
        n.CONTENT = note['content']
        n.USER_ID = note['user_id']
        n.CREATE_DATE = datetime.datetime.today()
        n.UPDATE_DATE = datetime.datetime.today()
        n.save()
