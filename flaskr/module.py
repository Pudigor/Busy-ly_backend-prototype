from . import db

class Messages(db.Model):                                   #Class Messages to create a database of messages
    id = db.Column(db.Integer, primary_key=True)            #Messages unique id
    sender_id = db.Column(db.Integer, nullable=False)       #The "user id" of the sender ("user id" has not been implemented due to protyping)
    receiver_id = db.Column(db.Integer, nullable=False)     #The "user id" of the reciever (see above)
    text = db.Column(db.Text, nullable=False)               #Our variable responsible for storing the message itself

