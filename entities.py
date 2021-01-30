from mendeleev import element


class Atom:
    def __init__(self, symbol: str, neighbours: list):
        self.symbol = symbol
        self.number = element(symbol).atomic_number
        self.neighbours = neighbours  # list of integer atom indexes

    def get_symbol(self) -> str:
        return self.symbol

    def get_number(self) -> int:
        return self.number

    def get_neighbours(self) -> list:
        return self.neighbours


class resonanceStruct:
    def __init__(self):
        self.atoms = None  # list of atom
        self.double_bonds = None  # list of tuples(atom index, atom index)
