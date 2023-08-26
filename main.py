import os

import streamlit as st
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from backend import generate_response
from prompt import prompt , intro
from PIL import Image
import random

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

key=os.environ["OPENAI_API_KEY"]

st.set_page_config(page_title="🤖 🧠 💬 Ravansha")
# login to profile
with st.sidebar:
    st.title("🙍‍♂️ 🧠 🤖 Ravansha")
    img = Image.open('ravan.jpg')
    st.image(img) 
    f =st.text_area('send me feedback')
    s = st.button('send')
    if s :
       print(f)
    st.write('Telegram bot feedback')
    st.write('https://t.me/TheYeChiziBegoBot?start=BONn99kt1b')
    st.markdown(intro())
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to Ravansha ☺️"}
    ]
if "buffer_memory" not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferWindowMemory(
        k=7, return_messages=True
    )
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input,)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(user_input, prompt(),key)
            st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
