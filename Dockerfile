FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD gunicorn core.wsgi:application --bind 0.0.0.0:8000