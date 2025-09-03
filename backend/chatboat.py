import os
from  groq import Groq

client =Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Chatboat (Groq Streaming): Type 'quit', exit or bye to stop\n")

def get_response(prompt: str) -> str:
    """Generate a response from Groq API using a supported model."""
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Updated model ID
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        stream=True
    )

    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
    return response


if __name__ == "__main__":
    print("Chatbot (Groq Streaming): Type 'quit', 'exit', or 'bye' to stop\n")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ['quit', 'exit', 'bye']:
            print("\nChatbot: Goodbye!")
            break
        reply = get_response(prompt)
        print("Chatbot:", reply)