from flask import (
    Flask,
    render_template,
)
from views.about import about_app


app = Flask(__name__)
app.register_blueprint(about_app, url_prefix="/about")


@app.get("/")
def get_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
