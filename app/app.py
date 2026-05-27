import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.gemini_service import generate_response

# page config
st.set_page_config(
    page_title="AI Career Advisor Chatbot",
    page_icon="🤖"
)


# title
st.title("🤖 AI Career Advisor Chatbot")


# load system prompt
with open("prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()


# session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# user input
user_input = st.chat_input("Ask your career question...")


if user_input:

    # show user message
    with st.chat_message("user"):
        st.markdown(user_input)


    # save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    # loading spinner
    with st.spinner("Generating response..."):

        response = generate_response(
            user_input=user_input,
            system_prompt=system_prompt,
            chat_history=st.session_state.messages
        )


    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(response)


    # save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })