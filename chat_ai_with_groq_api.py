from groq import Groq

# Initialize Groq API client
client = Groq(
    api_key= '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',
)

# Function to get chat completion from Groq API
def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Main loop for user input
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break
    response = get_ai_response(user_input)
    print("AI: " + response)