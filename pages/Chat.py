import streamlit as st
from utils.data_ingestion import load_data
from utils.embedding import download_gemini_embedding
from utils.model_api import load_model

# Streamlit app configuration
st.set_page_config(
    page_title="DataChat AI",
    page_icon="logo.png",
    layout="wide"
)

gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Function to load the query engine
def load_query_engine(docs):
    document = load_data(docs)
    model = load_model(gemini_api_key)
    query_engine = download_gemini_embedding(model, document)
    return query_engine

# Session state to store the query engine and chat history
if "query_engine" not in st.session_state:
    st.session_state["query_engine"] = None
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Callback to reload the query engine
def reload_query_engine():
    if st.session_state["uploaded_docs"]:
        st.session_state["query_engine"] = load_query_engine(st.session_state["uploaded_docs"])

# Initialize reset_session in session state if not already done
if "reset_session" not in st.session_state:
    st.session_state["reset_session"] = False

# Enhanced File Uploader
st.markdown("### 📂 Upload Your Documents")
if st.session_state["reset_session"]:
    # Clear the uploaded_docs indirectly by reinitializing the widget
    st.session_state.pop("uploaded_docs", None)  # Remove the key if it exists
    st.session_state["reset_session"] = False


uploaded_docs = st.file_uploader(
    "Supported formats: PDF, TXT, DOCX",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True,
    on_change=reload_query_engine,
    key="uploaded_docs"
)

if uploaded_docs:
    with st.spinner("Uploading and processing documents..."):
        st.session_state["query_engine"] = load_query_engine(uploaded_docs)
    st.success("Documents uploaded and processed successfully!")

# Chat Interface
if st.session_state["query_engine"]:
    # Clear History Button
    st.markdown("### 🗑️ Manage Your Session")
    if st.button("Clear History"):
        st.session_state["chat_history"] = []
        st.session_state["reset_session"] = True  # Set the reset flag
        st.session_state["query_engine"] = None
        st.success("Chat history and uploaded documents have been cleared!")
    st.subheader("💬 Chat with Your Documents")

    for message in st.session_state["chat_history"]:
        st.chat_message(message["role"]).write(message["content"])

    if user_message := st.chat_input("Type your question"):
        st.session_state["chat_history"].append({"role": "user", "content": user_message})
        st.chat_message("user").write(user_message)
        with st.spinner("Processing..."):
            response = st.session_state["query_engine"].query(user_message)
            bot_message = response.response
        st.session_state["chat_history"].append({"role": "assistant", "content": bot_message})
        st.chat_message("ai").write(bot_message)

# Centered Footer Section
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            background-color: #f9f9f9;
            padding: 10px 0;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <hr>
        © 2025 DataChat AI • <a href="mailto:rathiabhinav01@gmail.com" target="_blank">Contact Support</a> • <a href="https://github.com/Abhinav00711/DataChat-AI" target="_blank">Documentation</a>
    </div>
    """,
    unsafe_allow_html=True
)