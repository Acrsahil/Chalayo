from ollama import chat


def load_context():
    with open("context.txt", "r") as file:
        return file.read()


def chats(user_input):
    con = load_context()

    prompt = f"""
{con}

developer_mode = true

User: {user_input}
"""

    response = chat(
        model='gemma:2b',
        messages=[
            {'role': 'user', 'content': prompt}
        ],
    )

    return response.message.content


def main():
    print("Chatbot started (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Exiting chatbot...")
            break

        reply = chats(user_input)
        print("Bot:", reply)


if __name__ == "__main__":
    main()
