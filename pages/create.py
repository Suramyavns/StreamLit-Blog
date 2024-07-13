import streamlit as st
st.set_page_config(page_title='BlogBook',initial_sidebar_state='collapsed')
from st_pages import hide_pages
from datetime import datetime
from google.cloud import firestore
hide_pages(['main'])
def saveBlog():
    blog = {
        'title': st.session_state.title,
        'body': st.session_state.body,
        'date': firestore.SERVER_TIMESTAMP,
        'author': st.session_state.author
    }
    blogdb = st.session_state.blogs
    blogdb.create(blog)
with st.form('create-blog',clear_on_submit=True,border=True):
    st.header('Write your own blog!')
    header = st.columns([2,2])
    header[0].subheader('Title')
    header[0].text_input('Your title goes here...',placeholder='Lorem Ipsum',label_visibility='hidden',key='title')
    header[1].subheader("Author's Name")
    header[1].text_input('Your name goes here...',placeholder='John Doe',label_visibility='hidden',key='author')
    st.subheader('Body')
    st.text_area('.',label_visibility='hidden',placeholder='Your content goes here',key='body')
    if st.form_submit_button('Create',on_click=saveBlog):
        st.switch_page('pages/home.py')