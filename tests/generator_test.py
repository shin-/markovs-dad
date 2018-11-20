from markovs_dad.generator import Generator


def test_simple_generator():
    init_data = ['bowties are cool.']
    gen = Generator()
    assert gen.initialized is False
    gen.initialize_graph(init_data)
    assert gen.initialized is True

    assert gen.generate_chain() == 'bowties are cool.'
    assert gen.generate_chain(nmax=2) == 'bowties are'


def test_generator_loop():
    init_data = ['I am who I am']
    gen = Generator()
    gen.initialize_graph(init_data)

    assert gen.generate_chain(nmax=11) == (
        'I am who I am who I am who I am'
    )
