from urllib import request

from flask import Flask, render_template, request, jsonify

import requests

API_URL = "https://api-inference.huggingface.co/models/Writer/palmyra-small"
headers = {"Authorization": "Bearer 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"}


#syncing code base
app = Flask(__name__)

@app.route('/home')
def landing_page():
    return render_template('landing_page.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/poc')
def poc():
    return render_template('poc.html')


def chatbot_response(msg):
    response = requests.post(API_URL, headers=headers, json=msg)
    print(response.json())
    return response.json()

@app.route("/get", methods=["GET"])
def get_bot_response():
    userText = request.args.get('msg')

    generated_res = chatbot_response({
        "inputs": userText
    })

    print('this is printed',generated_res)

    return generated_res[0]['generated_text']




if __name__ == "__main__":
    app.run(debug=True)

