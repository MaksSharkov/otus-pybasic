"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import platform
from jsonplaceholder_requests import (
    fetch_users,
    fetch_posts,
)
from models import (
    Base,
    Session,
    User,
    Post,
    init_db,
)


async def create_users(session, users_list):
    users = [
        User(
            id=user.get("id"),
            username=user.get("username"),
            name=user.get("name"),
            email=user.get("email"),
        )
        for user in users_list
    ]
    session.add_all(users)
    await session.commit()


async def create_posts(session, posts_list):
    posts = [
        Post(
            id=post.get("id"),
            user_id=post.get("userId"),
            title=post.get("title"),
            body=post.get("body"),
        )
        for post in posts_list
    ]
    session.add_all(posts)
    await session.commit()


async def async_main():
    await init_db()
    users, posts = await asyncio.gather(
        fetch_users(["id", "name", "username", "email"]),
        fetch_posts(["id", "userId", "title", "body"]),
    )
    async with Session() as session:
        await create_users(session, users)
        await create_posts(session, posts)


def main():
    """
    Работаю на винде. У винды есть косяк с EventLoopPolicy и необходимо задать политику, чтобы не падал эксепшен при работе с asyncio
    https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    """
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
