import numpy as np
import matplotlib.pyplot as plt

def valid_reaction(reactives, products):
    reactives_atoms = {}
    for molecule, count in reactives:
        for atom, atom_count in molecule.atoms.items():
            if atom in reactives_atoms:
                reactives_atoms[atom]+=atom_count*count
            else:
                reactives_atoms[atom]=atom_count*count

    products_atoms = {}
    for molecule, count in products:
        for atom, atom_count in molecule.atoms.items():
            if atom in products_atoms:
                products_atoms[atom]+=atom_count*count
            else:
                products_atoms[atom]=atom_count*count

    return reactives_atoms==products_atoms

def kinetic_decomp(A0, k, T, steps=10, figure_path=None):
    time_points=np.linspace(0, T, steps)
    concentrations=A0*np.exp(-k*time_points)
    if figure_path is not None:
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, concentrations, 'b-', linewidth=2, marker='o')
        plt.xlabel("temps (en secondes)", fontsize=12)
        plt.ylabel("[A](t) en mol.L-1", fontsize=12)
        plt.title(f"Evolution [A](t)", fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(figure_path, dpi=150, bbox_inches='tight')
        plt.close()

    return concentrations
