# uvicorn main:app --host 0.0.0.0 --port 8000
FROM python:3.9-buster
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000