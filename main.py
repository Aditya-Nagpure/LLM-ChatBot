import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import time

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with NeoGPT!",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add custom CSS
st.markdown("""
    <style>
    .stChat message {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Add system message if not present
if not st.session_state.chat_history:
    system_msg = {
        "role": "system",
        "content": "You are NeoGPT, a helpful and knowledgeable AI assistant. Provide clear, accurate, and engaging responses."
    }
    st.session_state.chat_history.append(system_msg)

# Streamlit Title
st.title("🤖 NeoGPT - ChatBot")
st.markdown("---")

# Display the chat history (excluding system messages)
for message in st.session_state.chat_history:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input
user_prompt = st.chat_input("Ask NeoGPT...")

if user_prompt:
    try:
        # Add user's message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        st.chat_message("user").markdown(user_prompt)

        # Show typing indicator
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("🤔 Thinking...")

            try:
                # Call OpenAI API for a response
                response = client.chat.completions.create(
                    model="gpt-4",  # Use "gpt-3.5-turbo" for a cheaper option
                    messages=st.session_state.chat_history,
                    temperature=0.7,
                    max_tokens=2000,
                    stream=True
                )

                # Initialize variables for streaming response
                full_response = ""
                for chunk in response:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                        time.sleep(0.01)

                # Update with complete response
                message_placeholder.markdown(full_response)

                # Add AI response to chat history
                st.session_state.chat_history.append({"role": "assistant", "content": full_response})

            except Exception as e:
                error_message = f"Error: {str(e)}"
                message_placeholder.error(error_message)
                st.session_state.chat_history.pop()  # Remove the user message if API call failed

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add a clear chat button in the sidebar
with st.sidebar:
    if st.button("Clear Chat"):
        st.session_state.chat_history = [st.session_state.chat_history[0]]  # Keep only system message
        st.rerun()