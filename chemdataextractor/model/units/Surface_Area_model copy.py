# -*- coding: utf-8 -*-
"""
Units and models for Surface_Area.

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


class Surface_Area(Dimension):
    """
    Dimension subclass for Surface_Area.
    """
    pass

class Surface_AreaModel(QuantityModel):
    """
    Model for Surface_Area.
    """
    dimensions = Surface_Area()

class Surface_AreaUnit(Unit):
    """
    Base class for units with dimensions of Surface_Area.
    The standard value for Surface_Area is defined to be A/mgPt, implemented in the AmperePerMilligramPt class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(Surface_AreaUnit, self).__init__(Surface_Area(), magnitude, powers)

class AmperePerMilligramPt(Surface_AreaUnit):
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

# Dictionary to map unit symbols to unit classes for Surface_Area
units_dict_ma = {R(r'mgPt', group=0): AmperePerMilligramPt}
Surface_Area.units_dict = units_dict_ma
Surface_Area.standard_units = AmperePerMilligramPt()