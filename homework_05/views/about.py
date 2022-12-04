from flask import (
    Blueprint,
    render_template,
)

about_app = Blueprint(
    "about_app",
    __name__,
)

homeworks_list = [
    {"id": 1, "name": "Публикация репозитория и работа с функциями", "status": 2},
    {"id": 2, "name": "Классы и модули", "status": 2},
    {"id": 3, "name": "Docker контейнер c веб-приложением", "status": 2},
    {"id": 4, "name": "Асинхронная работа с сетью и БД", "status": 1},
    {"id": 5, "name": "Веб-приложение на Flask", "status": 1},
    {"id": 6, "name": "Взаимодействие между контейнерами", "status": 0},
    {"id": 7, "name": "Django проект", "status": 0},
    {"id": 8, "name": "Django Generics", "status": 0},
    {"id": 9, "name": "Тестирование Django приложения", "status": 0},
    {"id": 10, "name": "GitHub Actions", "status": 0},
    {"id": 11, "name": "GitLab pipelines", "status": 0},
]


@about_app.get("/")
def get_about():
    return render_template(
        "about.html",
        homeworks=homeworks_list,
    )
