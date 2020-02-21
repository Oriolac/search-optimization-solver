from typing import List

from search.definitions.interpretation import Interpretation

class Hanoi(Interpretation):
    def get_random_interpretation(self) -> Interpretation:
        pass

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


def main():
    return None