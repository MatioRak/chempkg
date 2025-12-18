import re
from chempkg.atom import elements

class Molecule:
    def __init__(self, formula : str):
        self.formula=formula
        self.atoms = self._analyse_formule(formula)
        self.weight = self._calcul_weight()

    def _analyse_formule(self, formula: str) -> dict:
        atoms_dict = {atom.name: atom for atom in elements}

        pattern = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(pattern, formula)

        result = {}

        for atom_symbol, count_str in matches:
            if not atom_symbol:
                continue

            if atom_symbol not in atoms_dict:
                raise ValueError(f"Atome inconnu: {atom_symbol}")

            atom = atoms_dict[atom_symbol]
            count = int(count_str) if count_str else 1

            # Ajouter ou incrémenter le compteur
            if atom in result:
                result[atom] += count
            else:
                result[atom] = count

        return result

    def _calcul_weight(self) -> float:
        total_weight = 0.0
        for atom, count in self.atoms.items():
            total_weight += atom.weight*count
        return total_weight

    def __repr__(self):
        return self.formula

    def __str__(self):
        atom=", ".join([f"{atom.name}: {count}" for atom, count in self.atoms.items()])
        return f"{self.formula} ({self.weight}g/mol) [{atom}]"

    def __eq__(self, other):
        if not isinstance(other, Molecule):
            return False
        return (self.formula==other.formula and self.atoms==other.atoms)
