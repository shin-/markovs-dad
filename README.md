# Markov's dad

A Markov chain generator for dad jokes. Source data from https://icanhazdadjoke.com/api

## Run the application

The easiest way to run the application is to do so using Docker Compose. You may refer to [Compose's install docs](https://docs.docker.com/compose/install/) for more information.

Simply clone this repository and run `docker-compose up --build` from the root directory. This will build and run the application inside a container. You can then point your browser (or use `curl`!) to [localhost:5000](http://localhost:5000) to get a computer's attempt at a dad joke. Just refresh the page if you wish to read another one!

### Run the application without Docker

If using Docker is not an option, you may do the following to run the application locally on your machine. Note that you will probably need Python 3.5 or above for it to work properly.

```
# first clone this repo and cd to the root directory
pip install -r requirements.txt
python setup.py install
python -m markovs_dad.main
```

## Test the application

To run the test suite inside a container, use the commands below:
```
docker build -t markovs_dad:test --target test .
docker run -t markovs_dad:test
```

You may also run the test suite directly from a Python dev environment with the `pytest tests/` command.