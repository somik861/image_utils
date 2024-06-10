from source.Command import Command
from source.common import load_image
from argparse import ArgumentParser, Namespace
from pathlib import Path

class CMD(Command):
    def __init__(self) -> None:
        super().__init__()

    def add_options(self, parser: ArgumentParser) -> None:
        parser.add_argument('image', type=Path)

    def run(self, args: Namespace) -> None:
        image = load_image(args.image)

        min_, max_, mean, stdev = image.min(), image.max(), image.mean(), image.std()

        print(f'shape: {image.shape}')
        print()
        print(f'min: {min_}')
        print(f'max: {max_}')
        print(f'mean: {mean}')
        print(f'std-dev: {stdev}')
