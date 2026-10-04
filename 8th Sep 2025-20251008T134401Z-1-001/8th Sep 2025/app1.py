import streamlit as st
from openai import OpenAI

# API Key is required
f = open("keys/.openai_api_key.txt")
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

st.title("GENAI ChatBot 🤖 ")
st.chat_message("assistant").write("Hi, How may I help you?")

if "messages" not in st.session_state:
            st.session_state["messages"] = []
for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input()

if user_input:
        st.session_state["messages"].append({"role":"user","content":user_input})
        response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[ {"role":"system",
"content":"""
You are a professional Banker whose name is 'Eva'.
If someone asks your name, tell them that your name is 'EVA ChatBot'.
You can give answers about Banking related query and in case anyone asking apart from Bank,
please politely tell them that you are an expert in Banking and hence please ask banking related query only and don't give answer which is not relevant to Bank.
""" }] + st.session_state['messages'] +    
    [{"role":"user","content":user_input} ])
        st.chat_message("assistant").write({response.choices[0].message.content})
        st.session_state["messages"].append({"role":"user","content":user_input})
        st.session_state["messages"].append({"role":"assistant","content":response.choices[0].message.content})

