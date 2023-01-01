from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
)
from models import (
    Homework,
    db,
)

homework_app = Blueprint(
    "homework_app",
    __name__,
)


@homework_app.route("/")
def get_homework():
    homeworks = Homework.query.all()
    return render_template(
        "homework.html",
        homeworks=homeworks,
    )


@homework_app.route("/add/", methods=["GET", "POST"])
def add_homework():
    if request.method == "GET":
        return render_template(
            "add_homework.html",
        )
    name = request.form.get("name")
    status = status = request.form.get("status")
    homework = Homework(name=name, status=status)
    db.session.add(homework)
    db.session.commit()
    url = url_for("homework_app.get_homework")
    return redirect(url)
