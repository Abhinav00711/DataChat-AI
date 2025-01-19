import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-1.5-pro' model.
    """
    try:
        logging.info("Model loading started...")
        model=Gemini(models='models/gemini-1.5-pro',api_key=GOOGLE_API_KEY)
        logging.info("Model loading completed...")
        return model
    except Exception as e:
        raise customexception(e,sys)