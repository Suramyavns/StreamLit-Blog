import streamlit as st
from libs.db import Users,Blogs,Tasks
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
print(st.session_state)
if 'users' not in st.session_state:
    st.session_state['users']=Users()
    if 'user' not in st.session_state:
        st.switch_page('./pages/login.py')

if 'blogs' not in st.session_state:
    st.session_state['blogs'] = Blogs()
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = Tasks()
st.switch_page('./pages/home.py')