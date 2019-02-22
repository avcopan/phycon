""" periodic table information
"""
from ._element_data import _SYMBOL_LST
from ._element_data import _ISOTOPIC_MASS_DCT


def standard_case(sym):
    """ get the standard capitalization of an element's atomic symbol
    """
    return str(sym).title()


def number(sym):
    """ get the atomic symbol
    """
    sym = standard_case(sym)
    return _SYMBOL_LST.index(sym)


def isotopic_mass(sym):
    """ get the atomic symbol
    """
    sym = standard_case(sym)
    return _ISOTOPIC_MASS_DCT[sym]
