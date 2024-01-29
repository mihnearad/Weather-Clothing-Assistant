import subprocess
import sys
from openai import OpenAI
import os 
from dotenv import load_dotenv
from weather import get_weather_info
from send_email import send_email

load_dotenv()

# Run the function to get weather information
question = get_weather_info()

# Continue with the rest of your main.py script
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

system_instruction = "You are a clothing assistant with a succinct and friendly attitude. You recommend the amount of layers and the thickness of them. You answer in 1 sentence."

openai_response = ""  # Initialize an empty string

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": question}
    ],
    stream=True,
)

# Capture the OpenAI response
openai_response = ""
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        openai_response += chunk.choices[0].delta.content


# Print the final OpenAI response
print(openai_response)


# Email the OpenAI response
subject = "How you should dress today:"
to_address = os.getenv("TO_EMAIL")

if to_address is None:
    print("Error: TO_EMAIL environment variable is not set.")
else:
    # Call the send_email function with the actual OpenAI response
    send_email(subject, openai_response, to_address)
