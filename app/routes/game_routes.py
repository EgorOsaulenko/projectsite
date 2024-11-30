from flask import Blueprint, render_template, redirect, url_for, request
from forms import GameForm, ReviewForm
from db.db_actions import add_game, get_games, get_game, add_review

game_bp = Blueprint("games", __name__)

@game_bp.route("/")
def index():
    return render_template("index.html")

@game_bp.route("/games/")
def games():
    games = get_games()
    return render_template("games.html", games=games)

@game_bp.route("/add-game/", methods=["GET", "POST"])
def add_game_route():
    form = GameForm()
    if form.validate_on_submit():
        add_game(title=form.title.data, price=form.price.data)
        return redirect(url_for("games.games"))
    return render_template("add_game.html", form=form)

@game_bp.route("/games/<int:game_id>/reviews/", methods=["GET", "POST"])
def reviews(game_id):
    form = ReviewForm()
    game = get_game(game_id)
    if not game:
        return redirect(url_for("games.games"))

    if form.validate_on_submit():
        add_review(game_id=game_id, reviewer=form.reviewer.data, text=form.text.data)
        return redirect(url_for("games.reviews", game_id=game_id))

    return render_template("reviews.html", game=game, form=form)

@game_bp.route("/games/")
def games():
    games = get_games()
    return render_template("games.html", games=games)

