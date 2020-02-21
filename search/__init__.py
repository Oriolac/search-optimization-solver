from search.nbsearch import main as nb
from search.srandom import main as random


def parser_algorithms(parser) -> None:
    parser.add_argument("algorithm", metavar="algorithm", help="Name of the algorithm to use", choices=["random", "nb"])
