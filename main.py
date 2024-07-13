import streamlit as st
from libs.db import App
from libs.db import CRUDBlogs

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
if 'app' not in st.session_state:
    st.session_state['app'] = App()
    st.session_state['blogs'] = CRUDBlogs()
st.switch_page('./pages/home.py')