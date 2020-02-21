import argparse
import sys
from typing import List
import search.definitions as defs


def parse_command_line_arguments(argv: List[str]) -> argparse.Namespace:
    parse = argparse.ArgumentParser(prog="python3 -m search",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse.add_argument("definition", metavar="definition", help="Name of the definition you want to optimize.")
    return parse.parse_args(args=argv)


if __name__ == '__main__':
    parser = parse_command_line_arguments(sys.argv[1:2])
    main = getattr(defs, parser.definition)
    main(sys.argv[2:])
