import streamlit as st
from streamlit_card import card
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
hide_pages(['main'])
st.title('Home')
if st.button('Write a blog!'):
    st.switch_page('pages/create.py')
blogdb = st.session_state.blogs
blogs = blogdb.readall()
container = st.container()
for blog in blogs:
    card(
        title=blog['title'],
        text=blog['body'],
    )