FROM python:3.14.0b2-alpine3.21

WORKDIR /app

RUN addgroup -g 1234 teste && \
    adduser -D -u 1234 -G teste thullyo

USER thullyo

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY app.py .

CMD [ "python", "app.py" ]