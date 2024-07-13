import streamlit as st
st.set_page_config(page_title='BlogBook',initial_sidebar_state='collapsed')
from st_pages import hide_pages
hide_pages(['home'])
def toHome(*args):
    blog = {
        'title':args[0],
        'author':args[1],
        'body':args[2],
        'date':f'{args[3]}'
    }
    st.switch_page('./pages/home.py')
with st.form('create-blog',clear_on_submit=True,border=True):
    st.header('Write your own blog!')
    header = st.columns([2,2])
    header[0].subheader('Title')
    title = header[0].text_input('Your title goes here...',placeholder='Lorem Ipsum',label_visibility='hidden')
    header[1].subheader("Author's Name")
    author_name = header[1].text_input('Your name goes here...',placeholder='John Doe',label_visibility='hidden')
    st.subheader('Body')
    body=st.text_area('.',label_visibility='hidden',placeholder='Your content goes here')
    st.subheader('Publish Date')
    date = st.date_input('Publish date',value='today',label_visibility='hidden')
    st.form_submit_button('Create',on_click=toHome,args=(title,author_name,body,date))