import argparse
import random
import sys
from typing import List, Optional

from search.definitions.interpretation import Interpretation


class Clause:

    def __init__(self, num_vars: int, clause_len: int) -> None:
        self.len: int = clause_len
        self.lits: List[int] = []
        self.get_random_clause(num_vars)

    def get_random_clause(self, num_vars: int) -> None:
        while len(self.lits) < self.len:
            new_lit = random.randint(1, num_vars)
            if new_lit not in self.lits:
                self.lits.append(new_lit)
        for i in range(len(self.lits)):
            if random.random() < 0.5:
                self.lits[i] *= -1


class CNF(Interpretation):

    def __init__(self, num_vars: int, num_clauses: int, clause_len: int, clauses: Optional[List[Clause]]) -> None:
        super().__init__()
        self.num_vars: int = num_vars
        self.num_clauses: int = num_clauses
        self.clause_len: int = clause_len
        if clauses is None:
            self.clauses: List[Clause] = []
            self.gen_random_clauses()
        else:
            self.clauses = clauses

    def gen_random_clauses(self) -> Interpretation:
        for i in range(self.num_clauses):
            c = Clause(self.num_vars, self.clause_len)
            self.clauses.append(c)
        return self

    def get_random_interpretation(self) -> Interpretation:
        for i in range(0, self.num_clauses - 1):
            lit = random.choice(self.clauses[i])
            op = random.choice([-1, 1])

        return None

    def cost(self) -> int:
        pass

    def copy(self) -> Interpretation:
        pass

    def print(self) -> None:
        pass

    def _get_list_neighbors(self) -> List[Interpretation]:
        pass

    def get_best_neighbor(self) -> Interpretation:
        pass

    def get_random_walk(self) -> List[Interpretation]:
        pass


def parse_command_line_arguments(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("problem", help="Problem.", type=str)
    parser.add_argument("num_vars", help="Number of vars", type=int)
    parser.add_argument("num_clauses", help="Num of clauses", type=int)
    parser.add_argument("clause_length", help="Length of clauses", type=int)

    return parser.parse_args(args=argv)


def main() -> None:
    parser = parse_command_line_arguments(sys.argv)
    kcnf = CNF(parser.num_vars, parser.num_clauses, parser.clause_length)
    module = __import__("search")
    search = getattr(module, parser.algorithm)
    search(kcnf)


if __name__ == '__main__':
    main()
