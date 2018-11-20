from markovs_dad.generator.graph import WeightedGraph


def test_simple_graph():
    wg = WeightedGraph()
    tick_node = wg.add_word('tick')
    tock_node = wg.add_word('tock', after=tick_node)
    assert tock_node.pick_follower() is None
    assert tick_node.pick_follower() == tock_node
    assert list(wg.starters) == [tick_node]


def test_loop_graph():
    wg = WeightedGraph()
    jan = wg.add_word('jan')
    ken = wg.add_word('ken', jan)
    pon = wg.add_word('pon', ken)
    jan2 = wg.add_word('jan', pon)
    assert jan == jan2
    assert jan.pick_follower() == ken
    assert ken.pick_follower() == pon
    assert pon.pick_follower() == jan
    assert list(wg.starters) == [jan]
