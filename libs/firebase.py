# firebase_module.py
import firebase_admin
from firebase_admin import credentials, auth, firestore, storage
import json,requests
import streamlit as st
from io import BytesIO

with open('config/general.json','r') as cf:
    configs = json.load(cf)
@st.cache_resource
def get_firebase_instance():
    return Firebase(
        cred_path='config/blogsite-firebase-config.json',
        storage_bucket=configs['storageBucket'],
        api_key=configs['apiKey']
    )


class Firebase:
    def __init__(self, cred_path, storage_bucket,api_key):
        # Initialize Firebase
        if not firebase_admin._apps:
            # Initialize Firebase with credentials and storage bucket
            self.cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(self.cred, {
                'storageBucket': storage_bucket  # This is where you specify the storage bucket name
            })
            self.db = firestore.client()
            self.bucket = storage.bucket()
            self.api_key = api_key
    # Authentication Methods
    def create_user(self, email, password):
        try:
            user = auth.create_user(email=email, password=password)
            return user
        except Exception as e:
            return str(e)

    def get_user(self, uid):
        try:
            user = auth.get_user(uid)
            return user
        except Exception as e:
            return str(e)

    def delete_user(self, uid):
        try:
            auth.delete_user(uid)
            return f'Successfully deleted user: {uid}'
        except Exception as e:
            return str(e)
    def get_current_user_data(self, id_token):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={self.api_key}"
        headers = {
            "Content-Type": "application/json"
        }
        payload = json.dumps({
            "idToken": id_token
        })
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()  # Return the user data
        else:
            return response.json()  # Return the error response
   
    def sign_in_with_email_and_password(self, email, password):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response.json()  # Return the sign-in response which includes idToken
        else:
            return response.json()  # Return the error response

    # Method to sign out (just a placeholder since sign out is client-side)
    def sign_out(self):
        st.session_state.pop('idToken')
        return "Sign out is handled on the client side by clearing the user's token."

    # Firestore Database Methods
    def add_data_to_firestore(self, collection, data):
        try:
            doc_ref = self.db.collection(collection)
            doc_ref.add(data)
            return f'Data added to Firestore: {data}'
        except Exception as e:
            return str(e)

    def get_data_from_firestore(self, collection, document):
        try:
            doc_ref = self.db.collection(collection).document(document)
            doc = doc_ref.get()
            if doc.exists:
                return doc.to_dict()
            else:
                return f'No such document in {collection}/{document}'
        except Exception as e:
            return str(e)

    def get_all_document_ids_by_user(self, collection,userid):
        try:
            col_ref = self.db.collection(collection)
            query = col_ref.where('user', '==', userid)
            docs = query.stream()
            ids = [doc.id for doc in docs]
            return ids
        except Exception as e:
            return str(e)
    def get_tasks_by_user(self, user_id):
        try:
            # Reference to the tasks collection
            col_ref = self.db.collection('tasks')
            # Query for tasks by user_id
            query = col_ref.where('user', '==', user_id)
            docs = query.stream()
            # Retrieve and return all matching documents
            tasks = [doc.to_dict() for doc in docs]
            return tasks
        except Exception as e:
            return str(e)
    def get_blogs_by_user(self, user_id):
        try:
            # Reference to the blogs collection
            col_ref = self.db.collection('blogs')
            # Query for blogs by user_id
            query = col_ref.where('author', '==', user_id)
            docs = query.stream()
            # Retrieve and return all matching documents
            blogs = [doc.to_dict() for doc in docs]
            return blogs
        except Exception as e:
            return str(e)
        
    def delete_document_from_collection(self, collection, document_id):
        try:
            doc_ref = self.db.collection(collection).document(document_id)
            doc_ref.delete()
            return f'Document with ID {document_id} successfully deleted.'
        except Exception as e:
            return str(e)
        
    # Storage Methods
    def upload_image(self, file_path, storage_path):
        try:
            image_file = BytesIO(file_path.read())
            blob = self.bucket.blob(storage_path)
            blob.upload_from_file(image_file, content_type=file_path.type)
            blob.make_public()
            return blob.public_url
        except Exception as e:
            return str(e)

    def download_image(self, storage_path, download_path):
        try:
            blob = self.bucket.blob(storage_path)
            blob.download_to_filename(download_path)
            return f'File {storage_path} downloaded to {download_path}'
        except Exception as e:
            return str(e)

    def delete_file(self, storage_path):
        try:
            blob = self.bucket.blob(storage_path)
            blob.delete()
            return f'File {storage_path} deleted from Firebase Storage'
        except Exception as e:
            return str(e)
