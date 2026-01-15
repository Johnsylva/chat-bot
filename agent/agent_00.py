from dotenv import load_dotenv
from openai import OpenAI
import yagmail
import os

load_dotenv('.env')
llm = OpenAI()


#configuration to setup yagmail to send an email
def send_email(body):
    yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), os.getenv("GMAIL_APP_PASSWORD"))
    yag.send(to="sylva.uwagboe@gmail.com", subject="TEST EMAIL", contents=body)

send_email('Testing 1, 2, 3')
