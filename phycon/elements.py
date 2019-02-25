""" periodic table information
"""
from ._element_data import _SYMBOL_LST
from ._element_data import _BONDING_VALENCE_DCT
from ._element_data import _ISOTOPIC_MASS_DCT


def element_keys():
    """ element keys
    """
    return _SYMBOL_LST


def organic_element_keys():
    """ organic element keys (elements with known standard bonding valences)
    """
    return tuple(_BONDING_VALENCE_DCT.keys())


def isotope_keys():
    """ isotope keys
    """
    return tuple(_ISOTOPIC_MASS_DCT.keys())


def standard_case(sym):
    """ standard capitalization of an element's atomic symbol
    """
    return str(sym).title()


def number(sym):
    """ atomic number / nuclear charge
    """
    sym = standard_case(sym)
    return _SYMBOL_LST.index(sym)


def isotopic_mass(sym):
    """ isotopic mass
    """
    sym = standard_case(sym)
    return _ISOTOPIC_MASS_DCT[sym]


def bonding_valence(sym):
    """ isotopic mass
    """
    sym = standard_case(sym)
    return _BONDING_VALENCE_DCT[sym]
