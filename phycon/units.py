""" unit conversions
"""
from scipy import constants as _constants
from scipy.constants import physical_constants as _physical_constants


EH2EV = _physical_constants['Hartree energy in eV'][0]
EH2WNUM = (_physical_constants['hartree-inverse meter relationship'][0]
           / 100.)
EH2KJ = (_physical_constants['hartree-joule relationship'][0]
         / 1000.
         * _constants.N_A)
EH2KCAL = EH2KJ / _constants.calorie
ANG2BOHR = _physical_constants['Bohr radius'][0] * 1.e10
RAD2DEG = 180. / _constants.pi
DEG2RAD = _constants.pi / 180.
