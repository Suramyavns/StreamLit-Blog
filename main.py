import streamlit as st
from libs.firebase import Firebase,get_firebase_instance
import json

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
app = get_firebase_instance()

try:
    st.session_state['userData'] = app.get_current_user_data(st.session_state.idToken)
    st.switch_page('./pages/home.py')
except:
    st.switch_page('./pages/login.py')
