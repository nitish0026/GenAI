import streamlit as st
import google.generativeai as genai
import os
import time
import joblib

# Load the API KEY

with open("Keys/.gemini.txt") as f:
    key = f.read().strip()
genai.configure(api_key=key)

##################

if 'chat_id' not in st.session_state:
    st.session_state.chat_id = None
if 'chat_title' not in st.session_state:
    st.session_state.chat_title = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'gemini_history' not in st.session_state:
    st.session_state.gemini_history = []

# Create a chat id
new_chat_id = f'{time.time()}'
MODEL_ROLE ="ai"
AI_AVATAR_ICON ='🤖'

# Create data directory
os.makedirs('database', exist_ok=True)

# Load past chats 
try:
    past_chats: dict= joblib.load('database/past_chats_list')
except:
    past_chats = {}

# Sidebar: chat selection

with st.sidebar:
    st.write('# past chats')
    if st.session_state.chat_id is None:
        st.session_state.chat_id = st.selectbox('Pick a past chat',
                                                options=[new_chat_id] + list(past_chats.keys()),
                                                format_func= lambda x: past_chats.get(x, 'New Chat'),
                                                placeholder='_')
    else:
        st.session_state.chat_id = st.selectbox('Pick a past chat',
                                                options=[new_chat_id] + list(past_chats.keys()),
                                                format_func= lambda x: past_chats.get(x, 'New Chat' if x!= st.session_state.chat_id 
                                                                                      else st.session_state.chat_title or 'Current Chat'),
                                                placeholder='_')
    st.session_state.chat_title = f'ChatSession-{st.session_state.chat_id}'

# Load message history
try:
    st.session_state.messages = joblib.load(f'database{st.session_state.chat_id}-st_messages')
    st.session_state.gemini_history = joblib.load(f'database{st.session_state.chat_id}-gemini_messages')
except:
    st.session_state.messages = []
    st.session_state.gemini_history = []

# Gimini Model
model = genai.GenerativeModel('models/gemini-2.0-flash')
st.session_state.model = model
st.session_state.chat = model.start_chat(history=st.session_state.gemini_history)


st.write("# Chat with Google AI - Gemini")

for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=message.get('avatar')):
        st.markdown(message['content'])

# Prompt
if prompt := st.chat_input("Write your message here ......"):
    if st.session_state.chat_id not in past_chats:
        past_chats[st.session_state.chat_id] = st.session_state.chat_title
        joblib.dump(past_chats, 'database/past_chats_list')
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append(dict(role="user", content=prompt))
    try:
        response = st.session_state.chat.send_message(prompt)
        response_text = response.text
    except Exception as e:
        response_text = f" Error: {e}"

    with st.chat_message(name=MODEL_ROLE, avatar = AI_AVATAR_ICON):
        st.markdown(response_text)

    # store message and history
    st.session_state.messages.append(dict(role=MODEL_ROLE, content=response_text, avatar=AI_AVATAR_ICON))
    st.session_state.gemini_history = st.session_state.chat.history

    # store on database (your local machine)
    joblib.dump(st.session_state.messages, f'database{st.session_state.chat_id}-st_messages')
    joblib.dump(st.session_state.gemini_history, f"database{st.session_state.chat_id}-gemini_messages")






