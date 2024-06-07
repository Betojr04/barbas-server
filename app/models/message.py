from app import db

class Message(db.Document):
    name = db.StringField(required=True)
    phone = db.StringField(required=True)
    message = db.StringField(required=True)
