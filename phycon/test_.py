""" test phycon.elements
"""
import numpy
from phycon import elements


def test__standard_case():
    """ test elements.standard_case
    """
    assert elements.standard_case('CL') == 'Cl'
    assert elements.standard_case('cl') == 'Cl'


def test__number():
    """ test elements.number
    """
    assert elements.number('CL') == 17
    assert elements.number('cl') == 17


def test__symbol():
    """ test elements.symbol
    """
    assert elements.symbol(17) == 'Cl'



def test__isotopic_mass():
    """ test elements.isotopic_mass
    """
    assert numpy.isclose(elements.isotopic_mass('CL'), 34.968852721)
    assert numpy.isclose(elements.isotopic_mass('cl'), 34.968852721)


def test__bonding_valence():
    """ test elements.bonding_valence
    """
    assert elements.bonding_valence('CL') == 1
    assert elements.bonding_valence('cl') == 1


if __name__ == '__main__':
    test__symbol()
