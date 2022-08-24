import os
import openai
from flask import Flask, request
from random import choice

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
completion = openai.Completion()
session_prompt = "The following is a conversation with an AI that helps write dating app messages. The AI is intelligent, creative, and clever. The AI will not provide boring or typical messages which would be ignored by a human inundated with messages from other AIs.\n\nHuman: What's a good first message to send to Hannah. Her profile says she wants someone funny and she loves to snowboard.\nAI: Hi Hannah. Did you know that many resorts outlawed snowboarding when the sport was invented back in the 80's? It was also originally referred to as \"Snurfing\".\nHuman:  That's a great first message. How about another?\nAI: If both your parents need a kidney to live and you're the only match in the world - what would you do?\nHuman: I matched with someone on Tinder and she doesn't have any text on her profile. How should I start the conversation?\nAI:\n\nHey, I noticed you don't have any text on your profile. I'm guessing you're a bit of a mystery. That's actually really intriguing to me. I'm dying to know more about you.\nHuman: Not bad. What else you got?\nAI:\n\nAre you a fan of mind-bending puzzles? I've got one for you: If a mute person cries, does anyone hear it?\nHuman: That's what I'm looking for. Got any more messages like this one?\nAI:\n\nWhy don't we skip the small talk and you can tell me your deepest, darkest secret? I promise I won't judge.\nHuman: You're getting better at this! One more please. \n\nHuman:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt_text,
      temperature=1,
      max_tokens=100,
      top_p=1,
      best_of=3,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    conversation = response['choices'][0]['text']
    return str(conversation)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
