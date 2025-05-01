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

# ---- Bible Verse Fetcher ----
def generate_bot_reply(prompt):
    verse_ref = prompt.strip()
    api_url = f"https://bible-api.com/{verse_ref.replace(' ', '%20')}"

    try:
        with st.spinner("🔍 Searching Scripture..."):
            response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            text = data.get("text", "").strip().replace("\n", " ")  # flatten text
            reference = data.get("reference", "")
            if text:
                return f"📖 **{reference}**: {text}"
            else:
                return "⚠️ Verse found but no content returned. Try rephrasing."
        else:
            return "⚠️ I couldn't find that verse. Please check your reference (e.g., John 3:16)."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

# ---- Send Message Handler ----
def send_message(user_input):
    user_input = user_input.strip()
    if user_input == "":
        return

    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate and store bot reply
    response = generate_bot_reply(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Set a flag to skip the main input temporarily
    st.session_state.message_sent = True

# ---- Display Chat History ----
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- Input Section ----
col1, col2 = st.columns([9, 1])

with col1:
    if not st.session_state.get("message_sent", False):
        user_input = st.text_input(
            label="Ask a question or type a verse (e.g., 'John 3:16')",
            key="main_input",
            label_visibility="collapsed"
        )
    else:
        # Dummy input to avoid rerun issues
        st.text_input("dummy", value="", label_visibility="collapsed", key="dummy_input")
        user_input = None
        st.session_state.message_sent = False  # Reset flag

with col2:
    if st.button("➡️", use_container_width=True) and user_input:
        send_message(user_input)
