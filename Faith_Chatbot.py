import streamlit as st

# ---- Chatbot Config ----
CHATBOT_NAME = "FaithBot -Created by Sothing Shimrah"

# ---- Session Initialization ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- Page Config ----
st.set_page_config(page_title="FaithBot - Your Bible Companion", layout="centered")
st.title(f"💬 {CHATBOT_NAME}")
st.markdown("Ask a question or share a thought related to faith, scripture, or Christian living.")

# ---- Display Chat History ----
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- User Input + Send Trigger ----
def send_message():
    user_input = st.session_state.user_input.strip()
    if user_input == "":
        return
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate bot response (placeholder)
    response = generate_bot_reply(user_input)
    # Save and display bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
    # Clear input box
    st.session_state.user_input = ""

# ---- Placeholder Response Generator ----
import requests

def generate_bot_reply(prompt):
    verse_ref = prompt.strip()
    api_url = f"https://bible-api.com/{verse_ref.replace(' ', '%20')}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            text = data.get("text", "").strip()
            reference = data.get("reference", "")
            return f"📖 **{reference}**\n\n{text}"
        else:
            return "⚠️ Sorry, I couldn't find that verse. Please check your reference (e.g., John 3:16)."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"


# ---- Input Field with Enter + Send Arrow ----
col1, col2 = st.columns([9, 1])
with col1:
    st.text_input("Type your message", key="user_input", label_visibility="collapsed", on_change=send_message)
with col2:
    if st.button("➡️", use_container_width=True):
        send_message()
