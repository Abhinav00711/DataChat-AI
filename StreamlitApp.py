import streamlit as st
from utils.data_ingestion import load_data
from utils.embedding import download_gemini_embedding
from utils.model_api import load_model

gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Function to load the query engine
def load_query_engine(docs):
    document = load_data(docs)
    model = load_model(gemini_api_key)
    query_engine = download_gemini_embedding(model, document)
    return query_engine

# Streamlit app configuration
st.set_page_config(
    page_title="DataChat AI",
    page_icon="logo.png",
    layout="wide"
)

# Header with logo and introduction
col1, col2 = st.columns([1, 4],vertical_alignment="center")
col1.image("logo.png", width=200)
col2.title("DataChat AI")
col2.subheader("Bringing Your Documents to Life")
st.write(
    """
    Welcome to **DataChat AI**, your intelligent assistant for extracting valuable insights from your documents. 
    Upload your files, ask questions, and interact with your data in real time. Perfect for students, researchers, 
    and professionals seeking a smarter way to engage with their information.
    """
)

# Session state to store the query engine and chat history
if "query_engine" not in st.session_state:
    st.session_state["query_engine"] = None
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Callback to reload the query engine
def reload_query_engine():
    if st.session_state["uploaded_docs"]:
        st.session_state["query_engine"] = load_query_engine(st.session_state["uploaded_docs"])

# File uploader section
st.markdown("### Upload Your Documents")
uploaded_docs = st.file_uploader(
    "Upload one or more documents",
    type=["pdf", "txt"],
    accept_multiple_files=True,
    on_change=reload_query_engine,
    key="uploaded_docs"
)

# Chat interface
if st.session_state["query_engine"]:
    st.subheader("Chat with your documents")

    for message in st.session_state["chat_history"]:
        st.chat_message(message["role"]).write(message["content"])

    if user_message := st.chat_input("Type your question"):
        # Add user message to the chat history
        st.session_state["chat_history"].append({"role": "user", "content": user_message})

        st.chat_message("user").write(user_message)
        
        # Get the response from the query engine
        with st.spinner("Processing..."):
            response = st.session_state["query_engine"].query(user_message)
            bot_message = response.response

        # Add bot response to the chat history
        st.session_state["chat_history"].append({"role": "assistant", "content": bot_message})
        
        # Display the latest message
        st.chat_message("ai").write(bot_message)