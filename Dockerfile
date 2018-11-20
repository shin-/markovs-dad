FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY setup.py ./
COPY markovs_dad ./markovs_dad/
RUN python setup.py install
CMD ["python", "-m", "markovs_dad.main"]
