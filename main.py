import openai
from fastapi import FastAPI, Form, Depends
from decouple import config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import google.generativeai as genai

from models import Conversation, SessionLocal
from utils import send_message, logger

app = FastAPI()
# openai.api_key = config("OPENAI_API_KEY")
genai.configure(api_key="AIzaSyD5K9BT5fIolElBIvDGSbFCrPpQW9e83GU")
whatsapp_number = config("TO_NUMBER")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/message")
async def reply(Body: str = Form(), db: Session=Depends(get_db)):
    # response = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",  # Use the latest model
    # messages=[{"role": "user", "content": Body}],  # Use "messages" format
    # max_tokens=200,
    # temperature=0.5,
    # )

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(Body)
    chat_response = response.text

    # print(chat_response)
    # chat_response = response["choices"][0]["message"]["content"].strip()

    try:
        conversation = Conversation(
            sender=whatsapp_number,
            message=Body,
            response=chat_response
        )

        db.add(conversation)
        db.commit()
        logger.info(f"Conversation #{conversation.id} stored in database")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error storing conversation in database: {e}")
    
    send_message(whatsapp_number, chat_response)
    return ""