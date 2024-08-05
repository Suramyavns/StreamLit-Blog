import streamlit as st
from streamlit_card import card
from datetime import datetime
from libs.firebase import get_firebase_instance

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
hide_pages(['main','login','create'])

app = get_firebase_instance()

st.title('Home')
if st.button('Write a blog!'):
    st.switch_page('pages/create.py')
if st.button('My task list'):
    st.switch_page('pages/tasks.py')
if st.button('Sign Out'):
    # Sign Out
    if 'idToken' in st.session_state:
        app.sign_out()
        st.switch_page('pages/login.py')
try:
    blogs = app.get_blogs_by_user(st.session_state.userData['users'][0]['email'])
    for blog in blogs:
            c = st.container(border=1)
            data = blog
            date = str(blog['date'])
            year = date[:4]
            month = date[5:7]
            day = date[8:10]
            c.header(blog['title'])
            c.image(blog['headerimg'])
            c.write(blog['body'])
            c.write(f"Published on {day}-{month}-{year} by {blog['author']}")
except Exception as e:
    st.write('OOPS!')
    print(e)