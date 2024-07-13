import streamlit as st
from st_pages import hide_pages
st.set_page_config(page_title='BlogBook',initial_sidebar_state='collapsed')
from google.cloud import firestore
hide_pages(['main','login'])
def saveBlog():
    print(st.session_state)
    blog = {
        'title': st.session_state.title,
        'body': st.session_state.body,
        'date': firestore.SERVER_TIMESTAMP,
        'author': st.session_state.author
    }
    for key,value in blog.items():
        if value=='':
            st.error('Please fill all the fields')
            st.rerun()
    blogdb = st.session_state.blogs
    blogdb.create(blog)
with st.form('create-blog',clear_on_submit=False,border=True):
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