# ChemPkg - Package Python 

Package Python pour modéliser des concepts chimiques fondamentaux : atomes, molécules et réactions chimiques.

**Projet Python ISDS - ISUP 2025**

---

## Structure du Projet

```
chempkg/
├── .gitignore
├── README.md 
├── chempkg/
│   ├── atom.py              
│   ├── mol.py              
│   └── reaction_utils.py   
└── tests/
    ├── test_atom.py
    ├── test_mol.py
    └── test_reaction_utils.py
```

---

## Installation et Tests

### Lancer les tests

```bash
# Tous les tests
python -m pytest tests/ -v
```

### Vérifier la qualité du code

```bash
pylint chempkg/*.py
```

**Objectif** : Note pylint > 7/10

---

## Documentation

### 1. Classe `Atom`

Représente un atome chimique avec calcul automatique de la configuration électronique selon la **règle de Klechkowski**.

#### Attributs
- `name` (str) : Symbole de l'atome
- `num_electron` (int) : Nombre d'électrons 
- `weight` (float) : Masse atomique en g/mol 
- `elec_config` (tuple) : Configuration électronique

#### Méthodes spéciales
- `__repr__()` : Retourne le symbole de l'atome 
- `__str__()` : Retourne une représentation lisible 
- `__eq__()` : Compare deux atomes
- `__hash__()` : Permet d'utiliser l'atome comme clé de dictionnaire


### 3. Module `reaction_utils`

Fonctions pour valider les réactions chimiques et modéliser les cinétiques de décomposition.

#### Fonction `valid_reaction(reactives, products)`

Vérifie si une réaction chimique respecte la **loi de conservation de la masse** (même nombre d'atomes de chaque type dans les réactifs et les produits).

**Paramètres** :
- `reactives` : `list[tuple[Molecule, int]]` - Liste de tuples (molécule, quantité)
- `products` : `list[tuple[Molecule, int]]` - Liste de tuples (molécule, quantité)

**Retour** : `bool` - `True` si la réaction est équilibrée, `False` sinon

#### Fonction `kinetic_decomp(A0, k, T, steps=10, figure_path=None)`

Modélise la cinétique de décomposition d'une molécule selon une **cinétique d'ordre 1**.

**Paramètres** :
- `A0` (float) : Concentration initiale (mol/L)
- `k` (float) : Constante de vitesse de réaction (s⁻¹)
- `T` (float) : Temps total de la réaction (secondes)
- `steps` (int) : Nombre de points de mesure (défaut: 10)
- `figure_path` (str ou None) : Chemin pour sauvegarder le graphique (optionnel)

**Retour** : `numpy.ndarray` - Tableau des concentrations aux différents temps

## Exemple d'utilisation combinés

### Exemple : Vérifier la formation d'eau

```python
from chempkg.atom import H, O
from chempkg.mol import Molecule
from chempkg.reaction_utils import valid_reaction

# Créer les molécules
h2 = Molecule("H2")
o2 = Molecule("O2")
h2o = Molecule("H2O")

# Vérifier la réaction
print(valid_reaction([(h2, 2), (o2, 1)], [(h2o, 2)]))  # True

# Détails des molécules
print(f"H2: {h2.weight} g/mol")    # 2.0
print(f"O2: {o2.weight} g/mol")    # 32.0
print(f"H2O: {h2o.weight} g/mol")  # 18.0
```
---

## Détails techniques

### Configuration électronique (Règle de Klechkowski)

L'ordre de remplissage des orbitales suit :
```
1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s → 5f → 6d → 7p
```

Nombre maximal d'électrons par orbitale : **n_max = (2l + 1) × 2**
- Orbitale **s** (l=0) : 2 électrons
- Orbitale **p** (l=1) : 6 électrons
- Orbitale **d** (l=2) : 10 électrons
- Orbitale **f** (l=3) : 14 électrons

### Parser de formules chimiques

Utilise l'expression régulière : `r'([A-Z][a-z]?)(\d*)'`
- `[A-Z]` : Lettre majuscule (symbole de l'atome)
- `[a-z]?` : Optionnellement une minuscule (ex: Cl, Na)
- `\d*` : Optionnellement des chiffres (quantité)

---

## Auteur

**Projet Python ISDS - ISUP 2025**

Package développé dans le cadre du cours de Python (Septembre-Novembre 2025).

---

## Licence

Projet à usage éducatif uniquement.