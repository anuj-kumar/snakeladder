class SideEffect(object):
    source = None
    dest = None
    name = ''

    def __init__(self, source: int, destination: int, name: str):
        self.source = source
        self.dest = destination
        self.name = name
