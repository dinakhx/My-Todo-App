import streamlit as st
import Functions

todos = Functions.read_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    Functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My to do app")
st.write("Hello!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()


st.text_input(label='', placeholder="Add a new to do", on_change=add_todo, key='new_todo')
