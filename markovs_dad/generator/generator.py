from random import choice

from .graph import WeightedGraph


class Generator(object):
    """
        A Markov chain generator. It must be initialized using the
        initialize_graph method before it can be used.
    """
    def __init__(self):
        self.graph = WeightedGraph()
        self.initialized = False

    def initialize_graph(self, stream):
        """
            Initialize the internal graph using the provided data stream.
            The stream must be an iterable of strings. Each string must be
            a sentence or coherent group of sentences.
        """
        for sentence in stream:
            current_node = None
            for word in sentence.split():
                current_node = self.graph.add_word(word, current_node)
        self.initialized = True

    def generate_chain(self, nmax=25):
        """
            Generate a random sentence based on the seed data.
            The returned sentence will contain at most nmax words (default: 25)
        """
        node = choice(list(self.graph.starters))
        sentence = []
        while node:
            if nmax == 0:
                break
            sentence.append(node.word)
            node = node.pick_follower()
            nmax -= 1
        return ' '.join(sentence)
