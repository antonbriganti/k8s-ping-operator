FROM python:3.9-slim-buster as base
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM base as test
COPY . .
CMD python -m unittest discover -s tests

FROM test as lint 
COPY lint-requirements.txt lint-requirements.txt
RUN pip install -r lint-requirements.txt
CMD python -m black --diff --check src/ tests/

FROM base as app
WORKDIR /app
COPY ./src ./src
CMD python -m kopf run src/pingtest_operator.py