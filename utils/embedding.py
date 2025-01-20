from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.embeddings.gemini import GeminiEmbedding

import sys
from utils.exception import customexception
from utils.logger import logging

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("Embedding download started...")
        gemini_embed_model = GeminiEmbedding(model_name="models/text-embedding-004")
        #Configure the settings
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20
        
        logging.info("Indexing started...")
        index = VectorStoreIndex.from_documents(document, llm=model, embed_model=gemini_embed_model)
        # index.storage_context.persist()
        
        logging.info("Query engine creation started...")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)