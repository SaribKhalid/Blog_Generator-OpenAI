from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

def generateblog(ParagraphTopic):
    response = client.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = "Write a paragraph about the following topic: " + ParagraphTopic,
        max_tokens = 400,
        temperature = 0.5
    )

    retrieve_blog = response.choices[0].text

    return retrieve_blog


keep_writing = True

while keep_writing:
    answer = input("Want to write a paragraph?(Y for Yes/N for No): ")
    if (answer.upper() == 'Y'):
        paragraph_topic = input("What should the paragraph talk about?: ")
        print(f"{paragraph_topic}:\n{generateblog(paragraph_topic)}")
    else:
        keep_writing = False
