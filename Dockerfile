FROM python:3.8-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENV TOKEN $TOKEN
ENV WORD_COUNT $WORD_COUNT

CMD [  "python", "./main.py"]