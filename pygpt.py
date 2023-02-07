import openai
from pyfiglet import Figlet

custom_fig = Figlet(font='alligator2')
print(custom_fig.renderText('PyGpt'))
print("By CorryL\n")

# Define OpenAI API key
openai.api_key = ""

# Set up the model and prompt
model_engine = "text-davinci-003"
history = []

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=inp,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    output = completion.choices[0].text
    history.append((input, output))
    return history, output

# Generate a response
while True:
    try:
        prompt = input("\033[31mHuman: \033[0m")
        history, response = chatgpt_clone(prompt, history)
        print("\033[32mGpt: \033[0m" + response)
    except Exception as e:
        print("Errore:", e)
        continue
