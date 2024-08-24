import streamlit as st
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
app = get_firebase_instance()
def saveTask():
    task_date = st.session_state.task_date.strftime("%d-%m-%Y")
    task = {
        "date":task_date,
        'task':st.session_state.task,
        'user':st.session_state.userData['users'][0]['email']
    }
    app.add_data_to_firestore('tasks',task)
    return True
def deleteTask(id):
    app.delete_document_from_collection('tasks',id)
    st.rerun()
if st.button('Home'):
    st.switch_page('pages/home.py')
    st.rerun()
st.title('Add a Task')
with st.form('Add a Task',clear_on_submit=True):
    task = st.text_input('Task',key='task')
    date = st.date_input('Date',key='task_date')
    st.form_submit_button(label='Add Task',on_click=saveTask)

st.header('Your tasks')
for task in app.get_all_document_ids_by_user('tasks',st.session_state.userData['users'][0]['email']):
    data = app.get_data_from_firestore('tasks',task)
    c = st.container(border=1)
    details,btn = c.columns([10,2],vertical_alignment='center')
    details.write(f'Task Name: {data["task"]}')
    details.write(f'Due Date: {str(datetime.strptime(data["date"], "%d-%m-%Y"))[:10]}')
    if btn.button('Delete',key=task):
        deleteTask(task)            