import os
from dotenv import load_dotenv
import groq

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("API_KEY")

# Connect to Groq
client = groq.Client(api_key=api_key)

while True:
    # User query
    user_query = input("What would you like to ask?: ")

    # Create a chat object
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": user_query
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Process results in real-time
    result = []
    for chunk in completion:
        for choice in chunk.choices:
            result.append(choice.delta.content)

    # Wait for the stream to complete
    for chunk in completion:
        pass

    # Print the results
    print("Results:")
    for index, item in enumerate(result):
        print(item, end="")

    # Ready to receive a new question
    print("\nAsk another question!")

# This point will be reached only if the program is interrupted (e.g., with Ctrl + C)