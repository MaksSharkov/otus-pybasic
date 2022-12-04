# uvicorn main:app --host 0.0.0.0 --port 8000
# docker build -t homework_03:latest /path/to/homework_03
# docker run -d -p 8000:8000 --name msharkov_hw03 homework_03:latest
FROM python:3.9-buster
COPY ./requirements.txt /dependencies/
WORKDIR /dependencies
RUN pip install -r requirements.txt
COPY ./app /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000