from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship('Card', back_populates='board', lazy=True)
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict['title'],
            owner = data_dict['title'],
        )