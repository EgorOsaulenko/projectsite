from db import Session
from db.models import Game, Review

def add_game(title, price):
    with Session() as session:
        game = Game(title=title, price=price)
        session.add(game)
        session.commit()

def get_games():
    with Session() as session:
        return session.query(Game).all()

def get_game(game_id):
    with Session() as session:
        return session.query(Game).filter_by(id=game_id).first()

def add_review(game_id, reviewer, text):
    with Session() as session:
        review = Review(game_id=game_id, reviewer=reviewer, text=text)
        session.add(review)
        session.commit()
