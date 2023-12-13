import os
from flask import Flask, request
from elevenlabs import generate, set_api_key, play
from openai import OpenAI
client = OpenAI()

app = Flask(__name__)

@app.route('/narrate', methods=['POST'])
def generate_narration():
    data = request.get_json()
    prompt = "Você vai narrar minhas ações no Minecraft como no jogo 'A Stanley Parable'." +   "Great! this is the event: { " + data['event'] +"}; the narration:"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    
    resp.completion = completion.choices[0].message
    print(completion.choices[0].message)

    set_api_key("")
    audio = generate(
                    text=resp.completion,
                    voice="Bella",
                    model='eleven_monolingual_v1'
                )
    play(audio)
    return resp.completion


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
