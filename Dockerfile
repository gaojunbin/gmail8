FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install flask
RUN pip install -v -e .

ENV FLASK_ENV=production

EXPOSE 5000

CMD ["python", "reminder_server.py"]
