from ._db import db

class Language(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))