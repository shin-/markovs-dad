from .. import cache
from ..generator import Generator
from ..icanhazapi import Client

__generator = None


def populate_generator(use_cache=False):
    """
        Create and populate a Generator object with the API's data.
        This is essentially a singleton. Care should be applied when
        manipulating in a threaded environment.
    """
    global __generator

    __generator = Generator()

    if use_cache:
        serialized_graph = cache.load_graph_data()
        if serialized_graph is not None:
            __generator.load_graph(serialized_graph)
            return

    # In case of cache miss or if opted not to use caching
    api_client = Client()
    try:
        def joke_stream():
            for data in api_client.iterate_jokes():
                yield data['joke']

        __generator.initialize_graph(joke_stream())
        if use_cache:
            cache.save_graph_data(__generator.graph.serialize())
    finally:
        api_client.close()


def get_joke():
    """
        Generate a "joke" using the populated generator singleton.
    """
    if __generator is None:
        raise ValueError('populate_generator needs to be called first')
    return __generator.generate_chain() + '\n'
