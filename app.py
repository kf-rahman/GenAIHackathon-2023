from urllib import request

from flask import Flask, render_template

import requests

API_URL = "https://api-inference.huggingface.co/models/Writer/palmyra-small"
headers = {"Authorization": "Bearer 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"}


#syncing code base
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')


@app.route('/poc')
def poc():
    return render_template('poc.html')


def chatbot_response(msg):
    response = requests.post(API_URL, headers=headers, json=msg)
    print(response.json())
    return response.json()

@app.route("/poc", methods=["GET"])
def get_bot_response():
    userText = request.args.get('msg')
    print("is this coming here")
    generated_res = chatbot_response({
    "inputs": userText
})[0]['generated_text']
)

    return generated_res


if __name__ == "__main__":
    app.run(debug=True)

