import os
import openai
from flask import Flask, request
from random import choice

message_history = [{'role': 'system', 'content': "The following is a conversation with an AI that helps humans create interesting conversation starters. The AI is intelligent, creative, and clever. The AI will not provide boring nor conventional messages."}]

def ask(question, role="user", chat_log=""): #Uses OpenAI API to generate a response to the user's input and return the response.
    message_history.append({"role": role, "content": f"{question}"})   # Add the user input to the chat history
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    conversation = response['choices'][0]['text']
    message_history.append({"role": "assistant", "content": f"{conversation}"}) # Add the generated response to the chat history
    return str(conversation)

def append_interaction_to_chat_log(question, answer, chat_log=""): #Twilio code that appends the user's input and its response to the chat log. It then returns the updated chat log.
    role = "user" if chat_log == "" else "assistant"
    message_history.append({"role": role, "content": f"{question}"})
    message_history.append({"role": "assistant", "content": f"{answer}"})
    return chat_log + f"{question}\nAI: {answer}\n"