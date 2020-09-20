from flask import Blueprint, jsonify, request
from . import db
from .module import Messages

main = Blueprint('main', __name__)  #making a blueprint to support our application

@main.route('/send_message', methods=['POST'])
def send_message():
    message_data = request.get_json()       #getting a .json from the aplication

    new_message = Messages(sender_id=message_data['sender_id'], receiver_id=message_data['receiver_id'], text=message_data['text']) #transforms the .json recieved in a Message type

    #updates the database
    db.session.add(new_message)
    db.session.commit()
    
    return 'Sent', 201

@main.route('/messages/<int:send_id>/<int:receive_id>')
def messages(send_id, receive_id):

    messages_list = Messages.query.all() #gets all messages stored in the database (not optimal for big databases, but enough for testing)

    messages = [] 

    for message in messages_list: 

        #gets all messages in the list that the user has sent to a specific receiver and vice-versa
        if (message.sender_id == send_id and message.receiver_id == receive_id) or (message.receiver_id == send_id and message.sender_id == receive_id):
            messages.append({'sender_id': message.sender_id, 'receiver_id': message.receiver_id, 'text': message.text})

    return jsonify({'messages' : messages})