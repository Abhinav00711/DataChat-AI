import sys
from llama_index.llms.gemini import Gemini
from utils.exception import customexception
from utils.logger import logging

def load_model(api_key):
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-1.5-pro' model.
    """
    try:
        logging.info("Model loading started...")
        model=Gemini(models='models/gemini-1.5-pro',api_key=api_key)
        logging.info("Model loading completed...")
        return model
    except Exception as e:
        raise customexception(e,sys)