# This is a custom python package to handle CRUD Operations
from google.cloud import firestore
from google.cloud.firestore import FieldFilter
class App:
    def __init__(self) -> None:
        self.db = firestore.Client.from_service_account_json('config/blogsite-firebase-config.json')

class Users(App):
    def __init__(self) -> None:
        super().__init__()
        self.userdb = self.db.collection('users')
    def addUser(self,data):
        self.userdb.add(data)
        self.username = data['username']
    def getUser(self,username,password):
        return self.userdb.where(filter=FieldFilter('username','==',username)).where(filter=FieldFilter('password','==',password)).get()
class Blogs(App):
    def __init__(self):
        super().__init__()
        self.blogdb = self.db.collection('blogs')
    def create(self, data):
        update_time,blog_ref=self.blogdb.add(data)
    def readall(self):
        blogs = []
        docs = self.blogdb.stream()
        for doc in docs:
            blogs.append(doc.to_dict())
        return blogs