from flask import Flask
from routes.game_routes import game_bp
from db import create_db

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.register_blueprint(game_bp)

create_db()

if __name__ == "__main__":
    app.run(debug=True, port=3000)
