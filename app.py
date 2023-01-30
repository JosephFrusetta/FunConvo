from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, session
from funconvo import ask, append_interaction_to_chat_log

app = Flask(__name__)
app.config['SECRET_KEY'] = 'q3cfe1ed8fae309f222'

@app.route('/funconvo', methods=['POST']) #Twilio code that allows chatlogs to be sent via SMS and passed to OpenAI's API
def tinder():
    chat_log.clear()
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)
