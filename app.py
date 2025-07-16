import streamlit as st
import pandas as pd
import requests
import os

# Google Drive CSV download link
CSV_URL = "https://drive.google.com/uc?export=download&id=1EhyUAt5SdGLeZdpCoMsOZe7kk8tpTdxH"

# Download CSV if not already present
if not os.path.exists("chatbot_data.csv"):
    st.info("Downloading chatbot data... (only once)")
    response = requests.get(CSV_URL)
    with open("chatbot_data.csv", "wb") as f:
        f.write(response.content)

# Load CSV
data = pd.read_csv("chatbot_data.csv")
response_dict = dict(zip(data['statement'].astype(str).str.lower(), data['status']))

def get_response(user_input):
    user_input = user_input.lower()
    for key in response_dict:
        if key in user_input:
            return response_dict[key]
    return "I'm here to support you. Please tell me more."

# Streamlit UI
st.title("🧠 MindCare – Mental Health Chatbot")
st.write("Chat anonymously. I'm always here for you.")

user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.markdown(f"**MindCare Bot:** {response}")
