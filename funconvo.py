import os
import openai
from flask import Flask, request
from random import choice

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
completion = openai.Completion()
session_prompt = "The following is a conversation with an AI that helps humans create interesting conversation starters. \nThe AI is intelligent, creative, and clever. \nThe AI will not provide boring or typical messages which would be ignored by another human, inundated with messages from other AIs.\n\nHuman: I just met someone with a pink fanny pack. How do I start a conversation with them?\nAI: Did you know fanny packs were one of humankind's oldest accessories? Just make sure to call them bumbags if you ever go to Great Britain.\n\nHuman: There's someone in my cooking class that I want to start a conversation with. What should I say to them?\nAI: Cooking is such a great way to show someone you care. What's your favorite dish to cook at home?\n\nHuman: What's a good first message to send to Hannah. Her dating profile says she wants someone funny and she loves to snowboard.\n\nHuman:  That's a great first message. How about another?\nAI: If both your parents need a kidney to live and you're the only match in the world - what would you do?\n\nAI: Hi Hannah. Did you know that many resorts outlawed snowboarding when the sport was invented back in the 80's? It was also originally referred to as \"Snurfing\".\n\nHuman: Not bad. What else you got?\nAI: Are you a fan of mind-bending puzzles? I've got one for you: If a mute person cries, does anyone hear it?"

def ask(question, chat_log=None): #Interfacing with the OpenAI API
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt_text,
      temperature=1,
      max_tokens=200,
      top_p=1,
      best_of=3,
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
