import streamlit as st
from st_pages import hide_pages
from libs.db import Users,Blogs
st.set_page_config(page_title='Login',initial_sidebar_state='collapsed')
st.title('Sign In')
if 'user' in st.session_state:
    hide_pages(['main'])
else:
    hide_pages(['main','login','home','create'])
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
def loginUser():
    uname = st.session_state.username
    passwd = st.session_state.passwd
    if uname and passwd:
        userdb = st.session_state.users
        if not userdb.getUser(uname,passwd):
            st.error('Invalid Credentials')
        else:
            st.session_state['user'] = userdb.getUser(uname,passwd)
            if 'blogs' not in st.session_state:
                st.session_state['blogs'] = Blogs()
            return True
    else:
        st.error('Please fill all the fields.')
with st.form('user-login',clear_on_submit=True,border=True):
    username = st.text_input('Username',key='username',placeholder='John Doe')
    password = st.text_input('Password',type='password',key='passwd',placeholder='********')
    if st.form_submit_button('Sign-In',on_click=loginUser):
        st.switch_page('main.py')
