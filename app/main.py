from flask import Flask
from db import create_db

app = Flask(__name__)
app.secret_key = "supersecretkey"


create_db()

if __name__ == "__main__":
    app.run(debug=True, port=3000)

