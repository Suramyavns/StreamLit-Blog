import streamlit as st
from streamlit_card import card
from libs.db import Blogs,Users
st.set_page_config(page_title='BlogBook',initial_sidebar_state='collapsed')
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
from streamlit_card import card
from st_pages import hide_pages
def logout():
    if 'user' in st.session_state:
        del st.session_state.user
    print(st.session_state)
    st.session_state['users']=Users()
    st.session_state['blogs']=Blogs()
hide_pages(['main','login','create'])
st.title('Home')
if st.button('Write a blog!'):
    st.switch_page('pages/create.py')
if st.button('My task list'):
    st.switch_page('pages/tasks.py')
if st.button('Sign Out'):
    logout()
    st.switch_page('pages/login.py')
if 'blogs' in st.session_state:
    blogdb = st.session_state.blogs
    blogs = blogdb.readall()
    container = st.container()
    for blog in blogs:
        card(
            title=blog['title'],
            text=blog['body'],
        )