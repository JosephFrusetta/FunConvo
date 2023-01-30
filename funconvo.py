import os
import openai
from flask import Flask, request
from random import choice

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"
completion = openai.Completion()
session_prompt = "test"

def ask(question, chat_log=None): #Interfacing with the OpenAI API
    if chat_log is None:
        chat_log = session_prompt
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt_text,
      temperature=0.99,
      max_tokens=200,
      top_p=1,
      best_of=20,
      frequency_penalty=2,
      presence_penalty=1.7,
      stop=[" Human:", " AI:"]
    )
    conversation = response['choices'][0]['text']
    return str(conversation)

def append_interaction_to_chat_log(question, answer, chat_log=None): #Twilio code that appends a question and response to the chat log.
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'