from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()
#Creates an instance of the OpenAI client class so we can communicate with OpenAI's API
#Similar to how we initialize a class in ruby with person = Person.new


def text_sentiment(text):
    llm = OpenAI()
    response = llm.responses.create(
        model = "gpt-4.1-mini",
        temperature=1,
        input = f"Accept the sentiment of the text and return my emotion: {text}"
    )

    return response.output_text

user_input = input("Tell me the sentiment of the text: \n")

print(text_sentiment(user_input))




# see OpenAI's docs for where we get the llm.responses.create - https://github.com/openai/openai-python
