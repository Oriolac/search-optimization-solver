#! /usr/bin/env python3
from __future__ import annotations

from random import randint
from typing import List
import sys
import argparse
from .interpretation import Interpretation


class Queens(Interpretation):

    def __init__(self, N: int) -> None:
        super().__init__()
        self.N = N
        self.vars = list(range(self.N))
        self.get_random_interpretation()

    def get_random_interpretation(self) -> Queens:
        for i in range(self.N):
            self.vars[i] = randint(0, self.N - 1)
        return self

    def cost(self) -> int:
        total_cost = 0
        for num, row in enumerate(self.vars):
            for num2 in range(num + 1, self.N):
                if row == self.vars[num2] or abs(num - num2) == abs(row - self.vars[num2]):
                    total_cost += 1
                    break
        return total_cost

    def copy(self) -> Queens:
        c = Queens(self.N)
        c.vars = list(self.vars)
        return c

    def print(self) -> None:
        sys.stdout.write("+")
        for c in range(self.N):
            sys.stdout.write("---+")
        sys.stdout.write("\n")
        for r in range(self.N):
            sys.stdout.write("|")
            for c in range(self.N):
                if r == self.vars[c]:
                    sys.stdout.write(" X |")
                else:
                    sys.stdout.write("   |")
            sys.stdout.write("\n")
            sys.stdout.write("+")
            for c in range(self.N):
                sys.stdout.write("---+")
            sys.stdout.write("\n")

    def _get_list_neighbors(self) -> List[Interpretation]:
        nbs = []
        for i in range(self.N):
            new_nb = self.copy()
            value = randint(0, self.N - 2)
            if value >= new_nb.vars[i]:
                value += 1
            new_nb.vars[i] = value
            nbs.append(new_nb)
        return nbs

    def get_best_neighbor(self) -> Interpretation:
        nbs = self._get_list_neighbors()
        best_nb = None
        best_cost = self.N
        for inb, nb in enumerate(nbs):
            if nb.cost() < best_cost:
                best_nb = inb
                best_cost = nb.cost()
        return nbs[best_nb]

    def get_random_walk(self) -> List[Interpretation]:
        nbs = self._get_list_neighbors()
        return nbs[randint(0, len(nbs) - 1)]


def parse_command_line_arguments(argv: List[str]) -> argparse.Namespace:
    from search import parser_algorithms
    parser = argparse.ArgumentParser(prog="nqueens",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter, )

    parser.add_argument("N", help="Number of rows or columns in NxN chess", type=int)
    parser_algorithms(parser)
    parser.add_argument("--maxtries", metavar="num", help="Num max of tries of each loop", type=int)

    return parser.parse_args(args=argv)


def main(argv: List[str]) -> None:
    import search
    parser = parse_command_line_arguments(argv)
    queen = Queens(parser.N)
    search = getattr(search, parser.algorithm)
    search(queen)
