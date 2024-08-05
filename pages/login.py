import streamlit as st
from st_pages import hide_pages
from libs.firebase import get_firebase_instance


st.set_page_config(page_title='Login',initial_sidebar_state='collapsed')
st.title('Sign In')
st.session_state['loginTries']=0

app = get_firebase_instance()

if 'idToken' in st.session_state:
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
def loginUser(app):
    email = st.session_state.email
    passwd = st.session_state.passwd
    if email and passwd:
        try:
            sign_in_result = app.sign_in_with_email_and_password(email,passwd)
            if 'idToken' in sign_in_result:
                st.session_state['idToken'] = sign_in_result['idToken']
                st.session_state['userData']=app.get_current_user_data(sign_in_result['idToken'])
                st.switch_page('pages/home.py')
            else:
                st.session_state['loginTries']+=1
                st.warning('Invalid Credentials')
        except Exception as e:
            st.error('Server Error: 500. Try again later.')
            print(e)
    else:
        st.error('Please fill all the fields.')
with st.form('user-login',clear_on_submit=True,border=True):
    email = st.text_input('Email',key='email',placeholder='example@gmail.com')
    password = st.text_input('Password',type='password',key='passwd',placeholder='********')
    if st.form_submit_button('Sign-In'):
        loginUser(app)
