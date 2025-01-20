import streamlit as st

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