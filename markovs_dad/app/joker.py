from ..generator import Generator
from ..icanhazapi import Client

__generator = None


def populate_generator():
    global __generator
    api_client = Client()
    try:
        def joke_stream():
            for data in api_client.iterate_jokes():
                yield data['joke']

        __generator = Generator()

        __generator.initialize_graph(joke_stream())
    finally:
        api_client.close()


def get_joke():
    if __generator is None:
        raise ValueError('populate_generator needs to be called first')
    return __generator.generate_chain() + '\n'
