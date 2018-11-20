from random import choice

from .graph import WeightedGraph


class Generator(object):
    def __init__(self):
        self.graph = WeightedGraph()
        self.initialized = False

    def initialize_graph(self, stream):
        for sentence in stream:
            current_node = None
            for word in sentence.split():
                current_node = self.graph.add_word(word, current_node)
        self.initialized = True

    def generate_chain(self, nmax=25):
        node = choice(list(self.graph.starters))
        sentence = []
        while node:
            if nmax == 0:
                break
            sentence.append(node.word)
            node = node.pick_follower()
            nmax -= 1
        return ' '.join(sentence)
