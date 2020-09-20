from flask import Blueprint, jsonify, request
from . import db
from .module import Messages

main = Blueprint('main', __name__)

@main.route('/send_message', methods=['POST'])
def send_message():
    message_data = request.get_json()

    new_message = Messages(sender_id=message_data['sender_id'], receiver_id=message_data['receiver_id'], text=message_data['text'])

    db.session.add(new_message)
    db.session.commit()

    return 'Sent', 201

@main.route('/messages/<int:send_id>/<int:receive_id>') #Prototype function, works best with small databases
def messages(send_id, receive_id):

    messages_list = Messages.query.all()

    messages = []

    for message in messages_list: 

        if (message.sender_id == send_id and message.receiver_id == receive_id) or (message.receiver_id == send_id and message.sender_id == receive_id):
            messages.append({'sender_id': message.sender_id, 'receiver_id': message.receiver_id, 'text': message.text})

    return jsonify({'messages' : messages})