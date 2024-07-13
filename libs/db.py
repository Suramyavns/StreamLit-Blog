# This is a custom python package to handle CRUD Operations
from google.cloud import firestore
class App:
    def __init__(self) -> None:
        self.db = firestore.Client.from_service_account_json('config/blogsite-firebase-config.json')
class CRUDBlogs(App):
    def __init__(self):
        super().__init__()
        self.blogdb = self.db.collection('blogs')
    def create(self, data):
        update_time,blog_ref=self.blogdb.add({"title":data['title'],'author':data['author'],'body':data['body'],'date':data['date']})
    def readall(self):
        blogs = []
        docs = self.blogdb.stream()
        for doc in docs:
            blogs.append(doc.to_dict())
        return blogs