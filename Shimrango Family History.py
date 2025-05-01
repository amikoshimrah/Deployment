import streamlit as st
import time
import fitz  # PyMuPDF
import os

st.set_page_config(page_title="Shimrango Clan", layout="centered")
st.title("🤖 Shimrango Clan")

# Load and cache the PDF content
@st.cache_data
def load_pdf_text():
    file_path = "Brief History of Shimrang Clan.pdf"
    if not os.path.exists(file_path):
        return "History file not found."

    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

history_content = load_pdf_text()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input field state management
if "input_field" not in st.session_state:
    st.session_state["input_field"] = ""

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box and button
with st.container():
    col1, col2 = st.columns([10, 1])
    with col1:
        user_input = st.text_input("You:", key="input_field", label_visibility="collapsed", placeholder="Ask about Shimrango Clan...")
    with col2:
        send_clicked = st.button("➤", use_container_width=True)

# Handle input
if (st.session_state["input_field"] and not send_clicked) or send_clicked:
    user_input = st.session_state["input_field"].strip()
    if user_input != "":
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Simple keyword search in history
        keywords = user_input.lower().split()
        matched_lines = []
        for line in history_content.split('\n'):
            if any(word in line.lower() for word in keywords):
                matched_lines.append(line.strip())

        response = " ".join(matched_lines[:5]) if matched_lines else "Sorry, I couldn't find anything related to that in the history."

        # Stream response
        with st.chat_message("assistant"):
            response_container = st.empty()
            full_response = ""
            for word in response.split():
                full_response += word + " "
                response_container.markdown(full_response + "▌")
                time.sleep(0.03)
            response_container.markdown(full_response.strip())

        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response.strip()
        })

        # Clear input the safe way
        st.session_state.pop("input_field")
        st.experimental_rerun()
