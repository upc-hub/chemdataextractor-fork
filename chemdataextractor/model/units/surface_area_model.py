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


class SurfaceArea(Dimension):
    """
    Dimension subclass for current density.
    """
    pass

class SurfaceAreaModel(QuantityModel):
    """
    Model for current density.
    """
    dimensions = SurfaceArea()

class SurfaceAreaUnit(Unit):
    """
    Base class for units with dimensions of current density.
    The standard value for current density is defined to be mA/cm^2, implemented in the MilliAmperePerSquareCentimeter class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(SurfaceAreaUnit, self).__init__(SurfaceArea(), magnitude, powers)

class MilliAmperePerSquareCentimeter(SurfaceAreaUnit):
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

units_dict_cd = {R('m2', group=0): MilliAmperePerSquareCentimeter}
SurfaceArea.units_dict = units_dict_cd
SurfaceArea.standard_units = MilliAmperePerSquareCentimeter()