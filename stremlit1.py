import streamlit as st
from nlp12 import get_answer  # Import your custom Q&A function

st.set_page_config(
    page_title="Q&A Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title('Q&A Chatbot')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User input field
prompt = st.chat_input('Ask anything...')

if prompt:
    # Append user input to session state
    st.session_state["messages"].append({
        "role": "user",
        "content": prompt
    })

    # Get assistant response
    response = get_answer(prompt)

    # Append assistant's response to session state
    st.session_state["messages"].append({
        "role": "assistant",
        "content": response
    })

# Display chat history
for chat in st.session_state["messages"]:
    st.chat_message(chat["role"]).markdown(chat["content"])
