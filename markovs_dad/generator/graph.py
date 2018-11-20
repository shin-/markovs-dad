from collections import Counter
from random import choice


class WeightedGraphNode(object):
    def __init__(self, word):
        self.word = word
        self.followers = Counter()

    def add_follower(self, node):
        self.followers.update([node])

    def pick_follower(self):
        elements = list(self.followers.elements())
        if not elements:
            return None
        return choice(elements)


class WeightedGraph(object):
    def __init__(self):
        self.index = {}
        self.starters = set()

    def add_word(self, word, after=None):
        if word in self.index:
            node = self.index[word]
        else:
            node = WeightedGraphNode(word)
            self.index[word] = node

        if after is None:
            self.starters.add(node)
        else:
            after.add_follower(node)

        return node
