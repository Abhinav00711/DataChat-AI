from llama_index.core import SimpleDirectoryReader
import sys
from utils.exception import customexception
from utils.logger import logging
import os

def load_data(uploaded_files):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("Data loading started...")
        # Create a temporary directory to store uploaded files
        temp_dir = "temp_uploaded_files"
        os.makedirs(temp_dir, exist_ok=True)

        # Save each uploaded file to the temporary directory
        for uploaded_file in uploaded_files:
            temp_file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_file.read())

        # Use the temporary directory for SimpleDirectoryReader
        loader = SimpleDirectoryReader(temp_dir)
        documents = loader.load_data()

        # Clean up temporary directory after use
        for temp_file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, temp_file))
        os.rmdir(temp_dir)
        logging.info("Data loading completed...")
        return documents
    except Exception as e:
        logging.info("Exception in loading data...")
        raise customexception(e,sys)