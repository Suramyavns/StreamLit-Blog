import streamlit as st
from datetime import datetime
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
taskdb = st.session_state.tasks
username = st.session_state.user[0].to_dict()['username']
def saveTask():
    task_date = st.session_state.task_date.strftime("%d-%m-%Y")
    task = {
        "date":task_date,
        'task':st.session_state.task,
        'user':username
    }
    taskdb.create(task)
    return True
def deleteTask(id):
    taskdb.deleteOne(id)
    st.rerun()
if st.button('Home'):
    st.switch_page('pages/home.py')
st.title('Add a Task')
with st.form('Add a Task',clear_on_submit=True):
    task = st.text_input('Task',key='task')
    date = st.date_input('Date',key='task_date')
    st.form_submit_button(label='Add Task',on_click=saveTask)

st.header('Your tasks')
for task in taskdb.getUsersTasks(username):
    data = task.to_dict()
    col1,col2,col3 = st.columns(3,vertical_alignment='center')
    col1.write(f'Task Name: {data["task"]}')
    col2.write(f'Due Date: {str(datetime.strptime(data["date"], "%d-%m-%Y"))[:10]}')
    if col3.button('Delete',key=task.id):
        deleteTask(task.id)