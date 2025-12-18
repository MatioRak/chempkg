class Atom:
    def __init__(self, name : str, num_electron : int, weight : float):
        self.name=name
        self.num_electron=num_electron
        self.weight=weight
        self.elec_config=self._get_orbitales()

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.name} ({self.weight}, {self.num_electron})"

    def __eq__(self, other)->bool:
        return (self.name==other.name and
                self.num_electron==other.num_electron and
                self.weight==other.weight)

    def _get_orbitales(self)->tuple:
        sorted_orbitales = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),
                            (5,1),(6,0),(4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]

        orbitales_letters = {0:'s',1:'p',2:'d',3:'f'}
        # On commence avec Z electrons a disposer , que l’on va soustraire au fil des orbitales
        electrons_remaining = self.num_electron
        config = []

        for n,l in sorted_orbitales:
            if electrons_remaining <= 0:
                break

            max_electrons=(2*l+1)*2
            electrons_orbital=min(electrons_remaining,max_electrons)

            orbitales_letter=orbitales_letters[l]
            config.append(f"{n}{orbitales_letter}{electrons_orbital}")

            electrons_remaining-=electrons_orbital

        return tuple(config)

    def __hash__(self):
        return hash((self.name, self.num_electron, self.weight))

O=Atom(name="O", weight=16.0, num_electron=8)
C=Atom(name="C", weight=12.0, num_electron=6)
H=Atom(name="H", weight=1.0, num_electron=1)
N=Atom(name="N", weight=14.0, num_electron=7)
Ca=Atom(name="Ca", weight=40.0, num_electron=20)
P=Atom(name="P", weight=31.0, num_electron=15)
K=Atom(name="K", weight=39.0, num_electron=19)
S=Atom(name="S", weight=32.0, num_electron=16)
Na=Atom(name="Na", weight=23.0, num_electron=11)
Cl=Atom(name="Cl", weight=35.5, num_electron=17)
Fe=Atom(name="Fe", weight=55.8, num_electron=26)
I=Atom(name="I", weight=127.0, num_electron=53)
F=Atom(name="F", weight=19.0, num_electron=9)
Co=Atom(name="Co", weight=59.0, num_electron=27)
Mo=Atom(name="Mo", weight=96.0, num_electron=42)

elements = [O, C, H, N, Ca, P, K, S, Na, Cl, Fe, I, F, Co, Mo]
