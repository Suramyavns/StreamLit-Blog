import streamlit as st
from st_pages import hide_pages
from libs.db import Users
st.set_page_config(page_title='Login',initial_sidebar_state='collapsed')
hide_pages(['main'])
st.title('Sign In')
def loginUser():
    uname = st.session_state.username
    passwd = st.session_state.passwd
    if uname and passwd:
        userdb = st.session_state.users
        if not userdb.getUser(uname,passwd):
            st.error('Invalid Credentials')
        else:
            st.session_state['user'] = userdb.getUser(uname,passwd)
            st.switch_page('main.py')
    else:
        st.error('Please fill all the fields.')
with st.form('user-login',clear_on_submit=True,border=True):
    username = st.text_input('Username',key='username',placeholder='John Doe')
    password = st.text_input('Password',type='password',key='passwd',placeholder='********')
    st.form_submit_button('Sign-In',on_click=loginUser)
