"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url, fields=None):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        if fields:
            parsed_data = list()
            for elem in data:
                parsed_elem = dict()
                for field in fields:
                    parsed_elem[field] = elem.get(field)
                parsed_data.append(parsed_elem)
            return parsed_data
        else:
            return data


async def fetch_users(fields=None):
    users = await fetch_json(USERS_DATA_URL, fields)
    return users


async def fetch_posts(fields=None):
    posts = await fetch_json(POSTS_DATA_URL, fields)
    return posts
