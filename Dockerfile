FROM python:3.7 AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY setup.py ./
COPY markovs_dad ./markovs_dad/
RUN python setup.py install
CMD ["python", "-m", "markovs_dad.main"]

FROM base as test
COPY test-requirements.txt .
RUN pip install -r test-requirements.txt
COPY tests/ ./tests/
CMD ["pytest", "-v", "tests/"]
