import streamlit as st
import functions
st.title("ToDo App")
st.write("This app is to increase your productivity")

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state.todo + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input("ToDo for the list", placeholder="Enter todo here...", label_visibility="hidden", key='todo', on_change=add_todo)    

    

