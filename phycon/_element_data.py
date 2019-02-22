""" periodic table data
"""

_SYMBOL_LST = (
    'X', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg',
    'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
    'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
    'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In',
    'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm',
    'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
    'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'
)

_ISOTOPIC_MASS_DCT = {
    'X': 0.0, 'H': 1.007825035, 'He': 4.00260324, 'Li': 7.016003, 'Be':
    9.0121822, 'B': 11.0093054, 'C': 12.0, 'N': 14.003074002, 'O': 15.99491463,
    'F': 18.99840322, 'Ne': 19.9924356, 'Na': 22.9897677, 'Mg': 23.9850423,
    'Al': 26.9815386, 'Si': 27.9769271, 'P': 30.973762, 'S': 31.9720707, 'Cl':
    34.968852721, 'Ar': 39.9623837, 'K ': 38.9637074, 'Ca': 39.9625906, 'Sc':
    44.95591, 'Ti': 47.9479473, 'V': 50.9439617, 'Cr': 51.9405098, 'Mn':
    54.9380471, 'Fe': 55.9349393, 'Co': 58.9331976, 'Ni': 57.9353462, 'Cu':
    62.9295989, 'Zn': 63.9291448, 'Ga': 68.92558, 'Ge': 73.9211774, 'As':
    74.9215942, 'Se': 79.9165196, 'Br': 78.9183361, 'Kr': 83.911507, 'Rb':
    84.911794, 'Sr': 87.9056188, 'Y': 88.905849, 'Zr': 89.9047026, 'Nb':
    92.9063772, 'Mo': 97.9054073, 'Tc': 97.907215, 'Ru': 101.9043485, 'Rh':
    102.9055, 'Pd': 105.903478, 'Ag': 106.905092, 'Cd': 113.903357, 'In':
    114.903882, 'Sn': 119.9021991, 'Sb': 120.9038212, 'Te': 129.906229, 'I':
    126.904473, 'Xe': 131.904144, 'Cs': 132.905429, 'Ba': 137.905232, 'La':
    138.906347, 'Ce': 139.905433, 'Pr': 140.907647, 'Nd': 141.907719, 'Pm':
    144.912743, 'Sm': 151.919728, 'Eu': 152.921225, 'Gd': 157.924019, 'Tb':
    158.925342, 'Dy': 163.929171, 'Ho': 164.930319, 'Er': 165.93029, 'Tm':
    168.93421, 'Yb': 173.938859, 'Lu': 174.94077, 'Hf': 179.9465457, 'Ta':
    180.947462, 'W': 183.950928, 'Re': 186.955744, 'Os': 191.961467, 'Ir':
    192.962917, 'Pt': 194.964766, 'Au': 196.966543, 'Hg': 201.970617, 'Tl':
    204.974401, 'Pb': 207.976627, 'Bi': 208.980374, 'Po': 208.982404, 'At':
    209.987126, 'Rn': 222.017571, 'D': 2.014101779, '2H': 2.014101779, 'T':
    3.01604927, 'H3': 3.01604927, 'He3': 3.01602931, 'Li6': 6.0151214, 'B10':
    10.0129369, 'C13': 13.003354826, 'C14': 14.003241982, 'N15': 15.00010897,
    'O18': 17.9991603, 'O17': 16.9991312, 'F18': 18.000937, 'F19':
    18.998403163, 'Ne22': 21.9913831, 'Ne21': 20.9938428, 'Mg26': 25.9825937,
    'Mg25': 24.9858374, 'Si29': 28.9764949, 'Si30': 29.9737707, 'S34':
    33.96786665, 'S33': 32.97145843, 'S36': 35.96708062, 'Cl37': 36.96590262,
    'Ar36': 35.96754552, 'Ar38': 37.9627325
}