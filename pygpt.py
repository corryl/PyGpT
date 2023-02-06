import openai

banner = '''
  ____   __   __   ____    ____    _____
U|  _"\ u\ \ / /U /"___|uU|  _"\ u|_ " _|
\| |_) |/ \ V / \| |  _ /\| |_) |/  | |
 |  __/  U_|"|_u | |_| |  |  __/   /| |\
 |_|       |_|    \____|  |_|     u |_|U
 ||>>_ .-,//|(_   _)(|_   ||>>_   _// \\_
(__)__) \_) (__) (__)__) (__)__) (__) (__)
By CorryL\n'''

print(banner)

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
        prompt = input("Hello, how can I help you?\n\n")
        history, response = chatgpt_clone(prompt, history)
        print(response + "\n")
    except Exception as e:
        print("Errore:", e)
        continue
