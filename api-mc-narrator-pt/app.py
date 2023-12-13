import os
from flask import Flask, request
from elevenlabs import generate, set_api_key, play,voices
from openai import OpenAI
client = OpenAI()

app = Flask(__name__)

@app.route('/narrate', methods=['POST'])
def generate_narration():
    data = request.get_json()
    promt = "Você vai narrar minhas ações no Minecraft como no jogo 'A Stanley Parable' só que em portugues e oriente o jogador como ele deve agir e insulte de vez em quando a inteligencia dele de maneira sutil. Esses são os eventos: { " + data['event'] +"}; para narrar, de 2 á 3 frases"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": promt},
        ]
    )
    resp = completion.choices[0].message
    print(resp)

    set_api_key(print(os.environ['ELEVEN_KEY']))
    audio = generate(text=resp.content, 
                    voice="Bill",
                    model="eleven_multilingual_v2")
    play(audio)
    return resp.content


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)