import argparse

from search.nbsearch import main as nb
from search.srandom import main as random


def parser_algorithms(prog: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=prog,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter, )
    parser.add_argument("algorithm", metavar="algorithm", help="Name of the algorithm to use", choices=["random", "nb"])
    return parser



