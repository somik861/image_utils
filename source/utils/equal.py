from source.Command import Command
from source.common import load_image
from argparse import ArgumentParser, Namespace
from pathlib import Path
import numpy as np

class CMD(Command):
    def __init__(self) -> None:
        super().__init__()

    def add_options(self, parser: ArgumentParser) -> None:
        parser.add_argument('fst_file', type=Path)
        parser.add_argument('snd_file', type=Path)

    def run(self, args: Namespace) -> None:
        fst = load_image(args.fst_file)
        snd = load_image(args.snd_file)

        print(np.all(fst == snd))
