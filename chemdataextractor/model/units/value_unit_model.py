# -*- coding: utf-8 -*-
"""
Units and models for power density.

.. codeauthor:: hein htet (hein.htet.j1@f.mail.nagoya-u.ac.jp)

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


class ValueUnit(Dimension):
    """
    Dimension subclass for current density.
    """
    pass

class ValueUnitModel(QuantityModel):
    """
    Model for current density.
    """
    dimensions = ValueUnit()

class ValueUnitUnit(Unit):
    """
    Base class for units with dimensions of current density.
    The standard value for current density is defined to be mA/cm^2, implemented in the MilliAmperePerSquareCentimeter class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(ValueUnitUnit, self).__init__(ValueUnit(), magnitude, powers)

class MilliAmperePerSquareCentimeter(ValueUnitUnit):
    """
    Class for mA/cm^2.
    """

    def convert_value_to_standard(self, value):
        return value

    def convert_value_from_standard(self, value):
        return value

    def convert_error_to_standard(self, error):
        return error

    def convert_error_from_standard(self, error):
        return error

units_dict_cd = {R('W', group=0): MilliAmperePerSquareCentimeter}
ValueUnit.units_dict = units_dict_cd
ValueUnit.standard_units = MilliAmperePerSquareCentimeter()