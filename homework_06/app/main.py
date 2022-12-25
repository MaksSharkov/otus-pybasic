from flask import (
    Flask,
    render_template,
)
from views import homework_app
from models import db
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.register_blueprint(homework_app, url_prefix="/homework")
app.config.update(
    SQLALCHEMY_DATABASE_URI=(
        os.environ.get("SQLALCHEMY_DATABASE_URI")
        or "postgresql+psycopg2://makssh:asdf1234@localhost:5432/homework"
    ),
    SQLALCHEMY_ECHO=True,
)
db.init_app(app)
migrate = Migrate(app, db)


@app.get("/")
def get_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
