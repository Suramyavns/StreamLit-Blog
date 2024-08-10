import streamlit as st
from st_pages import hide_pages
from google.cloud import firestore
from libs.firebase import get_firebase_instance
st.set_page_config(page_title='BlogBook',initial_sidebar_state='collapsed')
hide_pages(['main','login'])
app = get_firebase_instance()
def saveBlog(image):
    title = st.session_state.title
    body = st.session_state.body
    image_name = f"blog_headers/{image.name}"
    if title and body and image_name:
        image_url = app.upload_image(image, image_name)
        blog = {
            'title': title,
            'body': body,
            'date': firestore.SERVER_TIMESTAMP,
            'author': st.session_state.userData['users'][0]['email'],
            'headerimg':image_url
        }
        app.add_data_to_firestore('blogs',blog)
        return True
    else:
        st.error("Please fill all the fields and upload an image.")
with st.form('create-blog',clear_on_submit=False,border=True):
    st.header('Write your own blog!')
    header = st.columns(1)
    header[0].subheader('Title')
    header[0].text_input('Your title goes here...',placeholder='Lorem Ipsum',label_visibility='hidden',key='title')
    st.subheader('Header Image')
    uploaded_image = st.file_uploader('.', type=['jpg', 'jpeg', 'png'],label_visibility='hidden')
    st.subheader('Body')
    st.text_area('.',label_visibility='hidden',placeholder='Your content goes here',key='body')
    if st.form_submit_button('Create'):
        saveBlog(uploaded_image)
        st.switch_page('pages/home.py')