import streamlit as st
import google.generativeai as genai
import os

#st.title("Dear ChatBOT")
#st.markdown("This is just a sample examples for learning purpose")
#if st.button("Send balloons"):
 #           st.balloons()

 # Page configuration
#st.set_page_config(page_title="Gemini AI ChatBot", page_icon="🤖",  layout="wide" )

# Page Title and Headers
st.title("🤖 Gemini AI ChatBOT")
st.caption("GenAI Apps powered by Google's Gemini Model")

# API Key
with st.sidebar:
 st.header("configuration")
 google_api_key = st.text_input("Enter your Google API Key here", type="password",key="google_api_key")

 if google_api_key:
  try:
   genai.configure(api_key=google_api_key)
   st.success("API key configuration successfully completed.")
  except Exception as e:
   st.error(f"Failed to configure API Key: {e}", icon="⚠️")
 else:
  st.warning("Plesae enter your correct api key here to start chating. ", icon="🚨")

# Chat History
if "messages" not in st.session_state:
 st.session_state.messages = [
  {"role":"assistant", "content":"Hello, I'm your GENAI assistant. How can I help you today?"}
 ]

 # Display Chat History
 for message in st.session_state.messages:
  with st.chat_message(message["role"]):
   st.markdown(message["content"])

# User input 

if prompt := st.chat_input("what would you like to ask?"):
 if not google_api_key:
  st.info("Please enter your Google API Key in the sidebar to continue.")
  st.stop()
  # add user message to session state and display it
  st.session_state.messages.append({"role":"user","content":prompt})
  with st.chat_message("user"):
   st.markdown(prompt)
  # Generate and display assistant response
  with st.chat_message("assistant"):
    try:
      with st.spinner("Thinking...."):
       model = genai.GenerativeModel("gemini_pro")
       response = model.generate_content(prompt)
       response_text = response.text
      st.markdown(response_text)
      st.session_state.messages.append({"role":"assistant", "content":response_text})
    except Exception as e:
     st.error(f"An error occured: {e}", icon="⚠️")

    
