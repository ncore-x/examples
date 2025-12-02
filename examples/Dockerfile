FROM ununtu:20.04

RUN apt-get update && apt get install -y \
    python3 \
    python3-pip

WORKDIR /app

COPY . /app

RUN pop3 install -r requirements.txt

ENV APP_PORT=8000

EXPOSE $APP_PORT

CMD ["python3", "app.py"]
