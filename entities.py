
# from mendeleev import element

class Atom:
    def __init__(self):
        self.number = None # atomic number
        self.neighbours = None # list of integer atom indexes
        self.hidden_charge = None  # int
        self.formal_charge = None  # int

class resonanceStruct:
    def __init__(self):
        self.atoms = None # list of atom
        self.double_bonds = None #list of tuples(atom index, atom index)
