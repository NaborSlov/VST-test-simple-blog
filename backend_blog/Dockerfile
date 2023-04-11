FROM python:3.11-slim

WORKDIR app/
#COPY backend_blog/requirements.txt .
COPY requirements.txt .

RUN pip install -r requirements.txt

#COPY backend_blog/ .
COPY . .

CMD gunicorn backend_blog.wsgi -b 0.0.0.0:8000