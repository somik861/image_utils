from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import TypeVar

import numpy as np
from source.Command import Command
from source.common import load_image

T = TypeVar('T')


class CMD(Command):
    def __init__(self) -> None:
        super().__init__()

    def add_options(self, parser: ArgumentParser) -> None:
        parser.add_argument('fst_file', type=Path)
        parser.add_argument('snd_file', type=Path)
        parser.add_argument('--print_locations', action='store_true', help='Print missmatch pixels location')

    def _check_property(self, fst: T, snd: T, name: str) -> bool:
        if fst == snd:
            return True

        print(f'Missmatch {name}: \'{fst}\' vs \'{snd}\'')
        return False

    def run(self, args: Namespace) -> None:
        fst = load_image(args.fst_file)
        snd = load_image(args.snd_file)

        if not self._check_property(fst.dtype, snd.dtype, 'type'):
            return
        if not self._check_property(fst.shape, snd.shape, 'shape'):
            return

        equal_map = fst == snd
        equal = np.all(equal_map)
        if not equal:
            total_elems = equal_map.size
            missmatch = total_elems - np.sum(equal_map)
            print(f'Missmatch in {missmatch} elements (out of {total_elems}) {missmatch / total_elems * 100.0 :.2f} %')
            diff = np.abs(fst.astype(np.float64) - snd.astype(np.float64))
            print(f'Average difference {diff.mean()}')
            print(f'Biggest difference {diff.max()}')
            print(f'Smallest difference {diff.min()}')

            if args.print_locations:
                print('Missmatch locations:')
                for row, col in zip(*np.where(equal_map == 0)):
                    print(f'Row: {row}; Col: {col}')
        else:
            print(f'Equal: {equal}')
