FROM python:3.9-slim-buster as base
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY ./src ./src
CMD python -m kopf run src/pingtest_operator.py