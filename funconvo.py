import os
import openai
from flask import Flask, request
from random import choice

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"
completion = openai.Completion()
session_prompt = "The following is a conversation with an AI that helps humans create interesting conversation starters. The AI is intelligent, creative, and clever. The AI will not provide boring nor conventional messages.\n\nHuman: I just met someone with a pink fanny pack. How do I start a conversation with them?\nAI: Did you know fanny packs were one of humankind's oldest accessories? Just make sure to call them bumbags if you ever go to Great Britain.\n\nHuman: What's a good first message to send to Hannah. Her dating profile says she wants someone funny and she loves to snowboard.\nAI: Hi Hannah. Did you know that many resorts outlawed snowboarding when the sport was invented back in the 80's? It was also originally referred to as \"Snurfing\".\n\nHuman:  That's a great first message. How about another?\nAI: If both your parents need a kidney to live and you're the only match in the world - what would you do?"

def ask(question, chat_log=None): #Interfacing with the OpenAI API
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