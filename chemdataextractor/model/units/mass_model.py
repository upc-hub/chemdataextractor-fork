# -*- coding: utf-8 -*-
"""
Units and models for mass.

.. codeauthor:: HeinHtet by automatic parser tool

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .quantity_model import QuantityModel
from .unit import Unit
from .dimension import Dimension
from ...parse.elements import R
import logging

log = logging.getLogger(__name__)


class mass(Dimension):
    """
    Dimension subclass for mass.
    """
    pass

class massModel(QuantityModel):
    """
    Model for mass.
    """
    dimensions = mass()

class massUnit(Unit):
    """
    Base class for units with dimensions of mass.
    The standard value for mass is defined to be A/mgPt, implemented in the AmperePerMilligramPt class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(massUnit, self).__init__(mass(), magnitude, powers)

class AmperePerMilligramPt(massUnit):
    """
    Class for A/mgPt.
    """

    def convert_value_to_standard(self, value):
        return value

    def convert_value_from_standard(self, value):
        return value

    def convert_error_to_standard(self, error):
        return error

    def convert_error_from_standard(self, error):
        return error

# Dictionary to map unit symbols to unit classes for mass
units_dict_ma = {R(r'mgPt', group=0): AmperePerMilligramPt}
mass.units_dict = units_dict_ma
mass.standard_units = AmperePerMilligramPt()