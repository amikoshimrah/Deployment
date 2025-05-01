import streamlit as st
import requests

# ---- Chatbot Config ----
CHATBOT_NAME = "FaithBot"

# ---- Session Initialization ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- Page Config ----
st.set_page_config(page_title=f"{CHATBOT_NAME} - Your Bible Companion", layout="centered")
st.title(f"💬 {CHATBOT_NAME}")
st.caption("Created by Sothing Shimrah")
st.markdown("Ask about a Bible verse (e.g., 'John 3:16') or share a thought related to faith.")

# ---- Display Chat History ----
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- Bible Verse API Integration ----
def generate_bot_reply(prompt):
    verse_ref = prompt.strip()
    api_url = f"https://bible-api.com/{verse_ref.replace(' ', '%20')}"

    try:
        with st.spinner("Searching Scripture..."):
            response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            text = data.get("text", "").strip()
            reference = data.get("reference", "")
            if text:
                return f"📖 **{reference}**\n\n{text}"
            else:
                return "⚠️ Verse found but no content returned. Try rephrasing."
        else:
            return "⚠️ I couldn't find that verse. Please check your reference (e.g., John 3:16)."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

# ---- Send Handler ----
def send_message():
    user_input = st.session_state.user_input.strip()
    if user_input == "":
        return
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and display bot response
    response = generate_bot_reply(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

    # Clear input
    st.session_state.user_input = ""

# ---- User Input Field ----
col1, col2 = st.columns([9, 1])
with col1:
    st.text_input("Ask a question or type a verse (e.g., 'John 3:16')",
                  key="user_input",
                  label_visibility="collapsed",
                  on_change=send_message)
with col2:
    if st.button("➡️", use_container_width=True):
        send_message()
