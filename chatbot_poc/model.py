import requests

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

user_input = input("what would you like to ask the bot?\n")


API_URL = "https://api-inference.huggingface.co/models/Writer/palmyra-small"
headers = {"Authorization": "Bearer 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"}


def ask_the_model(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = ask_the_model({
    "inputs": user_input
})


print(output[0]['generated_text'])