# DataChat AI

![DataChat AI Logo](logo.png)

**DataChat AI** is an intelligent platform that revolutionizes how you interact with documents. Built on advanced AI technologies like Llama Index and Gemini, it allows users to upload documents, ask questions, and extract valuable insights in real-time.

---

## Table of Contents
1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
4. [Access the Deployed Application](#access-the-deployed-application)
5. [Project Structure](#project-structure)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- **Smart Document Management**: Supports multiple file formats like PDF, TXT, and DOCX.
- **Real-Time AI Interaction**: Ask questions and receive instant answers using the power of AI embeddings.
- **Session Management**: Manage uploaded documents and chat history with ease.
- **User-Friendly Interface**: Intuitive design with a customizable theme for seamless user experience.
- **Advanced AI Models**: Leverages Llama Index and Gemini for embedding and querying.

---

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:

- Python 3.9+
- pip
- Git

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Abhinav00711/DataChat-AI.git
   cd DataChat-AI
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Configuration:**
   Create a `.streamlit/secrets.toml` file and add your Gemini API key:
   ```toml
   GEMINI_API_KEY = "your_gemini_api_key_here"
   ```

4. **Run the Application:**
   ```bash
   streamlit run Home.py
   ```

5. Open your browser and navigate to `http://localhost:8501` to access the application.

---

## Usage

1. Launch the app using the command above.
2. Upload one or more documents (PDF, TXT, or DOCX).
3. Use the chat interface to ask questions about the content.
4. View responses generated in real time.
5. Manage your session using the provided controls (e.g., clear history).

---

## Access the Deployed Application

Visit the live application: [DataChat AI](https://datachatai.streamlit.app/)

---

## Project Structure

```
abhinav00711-datachat-ai/
├── Home.py                    # Main app interface
├── logo.png                   # Project Logo
├── requirements.txt           # Dependencies
├── pages/
│   └── Chat.py                # Chat interface and functionality
├── utils/
│   ├── data_ingestion.py      # Handles document ingestion
│   ├── embedding.py           # Embedding logic for AI models
│   ├── exception.py           # Custom exception handling
│   ├── logger.py              # Logging setup
│   └── model_api.py           # API interaction for AI models
└── .streamlit/
    └── config.toml            # Streamlit theme configuration
```

---

## Technologies Used

- **Python 3.9**: Programming language.
- **Streamlit**: Framework for building interactive web applications.
- **Llama Index**: Document querying and indexing library.
- **Gemini Embeddings**: Advanced embedding models for document analysis.
- **pypdf** and **docx2txt**: For handling PDF and DOCX files.

---

## Contributing

We welcome contributions! Follow these steps to get started:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

For questions or support, contact [rathiabhinav01@gmail.com](mailto:rathiabhinav01@gmail.com) or visit the [documentation](https://github.com/Abhinav00711/DataChat-AI).
