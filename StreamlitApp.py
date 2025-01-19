import streamlit as st
from QA.data_ingestion import load_data
from QA.embedding import download_gemini_embedding
from QA.model_api import load_model

@st.cache_resource
def load_query_engine(doc):
    document=load_data(doc)
    model=load_model()
    query_engine=download_gemini_embedding(model,document)
    return query_engine

st.set_page_config("RAG(QA)",layout="wide")
st.header("QA with Documents(Information Retrieval)")
doc=st.file_uploader("Upload your documents",type=["pdf","txt"])
if doc:
    query_engine=load_query_engine(doc)
    user_question= st.text_input("Ask your question")
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            response = query_engine.query(user_question)
            st.write(response.response)