import openai
from sqlalchemy.orm import Session
from crud import update_translation_task
from dotenv import load_dotenv
import os
load_dotenv()
from dotenv import load_dotenv




OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def perform_translation(task: int , text : str ):


