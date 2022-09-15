import os
import openai
from flask import Flask, request
from random import choice

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
completion = openai.Completion()
session_prompt = "The following is a conversation with an AI that helps write interesting conversation starters. The AI is intelligent, creative, and clever. The AI will not provide boring or typical messages which would be ignored by a human inundated with messages from other AIs.\n\nHuman: What's a good first message to send to Hannah. Her dating profile says she wants someone funny and she loves to snowboard.\nAI: Hi Hannah. Did you know that many resorts outlawed snowboarding when the sport was invented back in the 80's? It was also originally referred to as \"Snurfing\".\n\nHuman:  That's a great first message. How about another?\nAI: If both your parents need a kidney to live and you're the only match in the world - what would you do?\n\nHuman: I matched with someone on a dating app and she doesn't have any text on her profile. How should I start the conversation?\nAI: Hey, I noticed you don't have any text on your profile. I'm guessing you're a bit of a mystery. That's actually really intriguing to me. I'm dying to know more about you.\n\nHuman: Not bad. What else you got?\nAI: Are you a fan of mind-bending puzzles? I've got one for you: If a mute person cries, does anyone hear it?\n\nHuman: That's what I'm looking for. Got any more messages like this one?\nAI: Why don't we skip the small talk and you can tell me your deepest, darkest secret? I promise I won't judge.\n\nHuman: I just met someone with a pink fanny pack. How do I start a conversation with them?\nAI: Did you know fanny packs were one of humankind's oldest accessories? Just make sure to call them bumbags if you ever go to Great Britain.\n\nHuman: I met someone really cool and into bikes. What should I say to them?\nAI: Did you know that if the number of cyclists tripled, the rate of motorist-bicycle accidents would be cut in half?"

def ask(question, chat_log=None): #Interfacing with the OpenAI API
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt_text,
      temperature=1,
      max_tokens=100,
      top_p=1,
      best_of=3,
      frequency_penalty=0.04,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    conversation = response['choices'][0]['text']
    return str(conversation)

def append_interaction_to_chat_log(question, answer, chat_log=None): #Twilio code that appends a question and response to the chat log.
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
