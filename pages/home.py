import streamlit as st
from streamlit_card import card
from datetime import datetime
from libs.firebase import get_firebase_instance
from libs.blogs import blogs as Blogs
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
    Blogs.display()
    blogs = app.get_all_blog_ids_by_user('blogs',st.session_state.userData['users'][0]['email'])
    for blog in blogs:
            data = app.get_data_from_firestore('blogs',blog)
            c = st.container(border=1)
            date = str(data['date'])
            year = date[:4]
            month = date[5:7]
            day = date[8:10]
            c.header(data['title'])
            c.image(data['headerimg'])
            publish_date,blank,delete_btn = c.columns([8,2,2],vertical_alignment='center')
            publish_date.write(data['body'])
            publish_date.write(f"Published on {day}-{month}-{year} by {data['author']}")
            if delete_btn.button('Delete',key=blog):
                app.delete_document_from_collection('blogs',blog)
                app.delete_file(data['headerimg'])
                st.rerun()
except Exception as e:
    st.write('OOPS!')
    print(e)