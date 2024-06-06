from argparse import ArgumentParser
import sys
from source.utils import equal
from source.Command import Command
from importlib import import_module
from pathlib import Path

COMMANDS: dict[str, Command] = {}

def _load_commands() -> None:
    sources = Path(__file__).parent/'source'/'utils'
    for cmd_file in sources.iterdir():
        if not cmd_file.is_file():
            continue
        if '__' in cmd_file.name:
            continue
        if cmd_file.suffix != '.py':
            continue

        cmd_cls: type[Command]
        cmd_cls = import_module(f'source.utils.{cmd_file.stem}').CMD
        COMMANDS[cmd_file.stem] = cmd_cls()

def main() -> int:
    _load_commands()

    parser = ArgumentParser()
    subp = parser.add_subparsers(title='operation', dest='operation', required=True)
    for name, cmd in COMMANDS.items():
        cmd.add_options(subp.add_parser(name))

    args = parser.parse_args()
    COMMANDS[args.operation].run(args)

    return 0

if __name__ == '__main__':
    sys.exit(main())