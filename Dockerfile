FROM python:3.10-slim

ENV PYTHONBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "pictures_store.wsgi"]
