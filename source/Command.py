from argparse import ArgumentParser, Namespace

class Command:
    def __init__(self) -> None:
        pass

    def add_options(self, parser: ArgumentParser) -> None:
        raise NotImplementedError

    def run(self, args: Namespace) -> None:
        raise NotImplementedError
