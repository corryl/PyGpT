import openai
import pyfiglet


ascii_banner = pyfiglet.figlet_format("PyGpt")
print(ascii_banner)
print("By CorryL\n")

# Define OpenAI API key
openai.api_key = ""

conversation_history = []

end_string = "exit"
clear_history_string = "clear"
print_history_string = "history"

print("\nexit - exit the application")
print("history - show the entire conversation")
print("clear - clear history\n")

while True:
    user_input = input(">> ")

    if user_input.strip().lower() == end_string:
        print("Bye!")
        break

    elif user_input.strip().lower() == clear_history_string:
        conversation_history = []
        print("History cleared!")

    elif user_input.strip().lower() == print_history_string:
        for i in conversation_history:
            print(i)

    else:
        conversation_history.append(f"You: {user_input}")

        conversation_context = '\n'.join(conversation_history[-5:])

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{user_input}\n{conversation_context}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text

        print(response)
        conversation_history.append(response)
