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
col2.markdown(
    """
    ## **DataChat AI**  
    ### *Bringing Your Documents to Life*
    Unleash insights from your documents with AI-powered chat.
    Upload, question, and discover effortlessly.
    """
)
st.markdown(
    """
    <style>
        .welcome-header {
            font-size: 28px;
            font-weight: bold;
            color: #333;
        }
        .welcome-subheader {
            font-size: 20px;
            color: #555;
            line-height: 1.6;
        }
        .welcome-highlight {
            font-size: 24px;
            font-weight: bold;
            color: #007BFF;
            margin-top: 20px;
        }
    </style>

    <div class="welcome-header">Welcome to <span style="color: #007BFF;">DataChat AI</span> – Your Intelligent Partner in Document Exploration and Insight Discovery!</div>
    <div class="welcome-subheader">
        🧠 <b>Transform How You Interact with Information</b><br>
        Say goodbye to hours of manual searching and sifting through endless pages. With <b>DataChat AI</b>, you can effortlessly extract valuable insights from your documents in real time.
        <br><br>
        🚀 <b>Unlock the Power of AI at Your Fingertips</b><br>
        Whether you're a student striving to ace your research, a professional streamlining workflows, or a curious mind exploring new ideas, our advanced tools powered by <b>Llama Index</b> and <b>Gemini</b> are here to help.
        <br><br>
        🌟 <b>Why Choose DataChat AI?</b><br>
        - 📂 <b>Smart Document Management</b>: Upload multiple files and let AI do the heavy lifting.<br>
        - 🔍 <b>Real-Time Interaction</b>: Ask questions, analyze data, and uncover insights in seconds.<br>
        - 🤝 <b>Tailored for Everyone</b>: Perfect for researchers, educators, professionals, and beyond!
        <br><br>
        ✨ <b>How It Works</b><br>
        1. Upload your documents (PDF, TXT or DOCX).<br>
        2. Ask questions or dive deep into specific topics.<br>
        3. Experience personalized, real-time answers powered by state-of-the-art AI.
    </div>
    <div class="welcome-highlight">Ready to revolutionize your workflow?<br>Start your journey with <b>DataChat AI</b> today – because smarter insights lead to smarter decisions.</div>
    """,
    unsafe_allow_html=True
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

# Enhanced File Uploader
st.markdown("### 📂 Upload Your Documents")
uploaded_docs = st.file_uploader(
    "Supported formats: PDF, TXT, DOCX",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True,
    on_change=reload_query_engine,
    key="uploaded_docs"
)

# Chat interface
if st.session_state["query_engine"]:
    st.subheader("💬 Chat with Your Documents")

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
