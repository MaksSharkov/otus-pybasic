from flask import (
    Blueprint,
    render_template,
)
from models import Homework

homework_app = Blueprint(
    "homework_app",
    __name__,
)


@homework_app.get("/")
def get_homework():
    homeworks = Homework.query.all()
    return render_template(
        "homework.html",
        homeworks=homeworks,
    )
