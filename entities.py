from mendeleev import element  # `pip install mendeleev`


class Atom:
    def __init__(self, symbol: str, neighbours: list, lone_pairs: int):
        self.symbol = symbol
        self.number = element(symbol).atomic_number
        self.neighbours = neighbours  # list of integer atom indexes
        self.valence_electrons = len(self.neighbours) + lone_pairs*2  # number of valence electrons on the atom.

    def get_symbol(self) -> str:
        return self.symbol

    def get_number(self) -> int:
        return self.number

    def get_neighbours(self) -> list:
        return self.neighbours

    def get_sigma_bonds(self) -> int:
        return len(self.neighbours)

    def get_valence_electrons(self) -> int:
        return self.valence_electrons


class resonanceStruct:
    def __init__(self):
        self.atoms = None  # list of atom
        self.double_bonds = None  # list of tuples(atom index, atom index)
