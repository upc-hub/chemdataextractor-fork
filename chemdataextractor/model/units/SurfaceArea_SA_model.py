# -*- coding: utf-8 -*-
"""
Units and models for SurfaceArea_SA.

.. codeauthor:: heinhtet by automatic parser tool

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


class SurfaceArea_SA(Dimension):
    """
    Dimension subclass for SurfaceArea_SA.
    """
    pass

class SurfaceArea_SAModel(QuantityModel):
    """
    Model for SurfaceArea_SA.
    """
    dimensions = SurfaceArea_SA()

class SurfaceArea_SAUnit(Unit):
    """
    Base class for units with dimensions of SurfaceArea_SA.
    The standard value for SurfaceArea_SA is defined to be A/mgPt, implemented in the AmperePerMilligramPt class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(SurfaceArea_SAUnit, self).__init__(SurfaceArea_SA(), magnitude, powers)

class AmperePerMilligramPt(SurfaceArea_SAUnit):
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

# Dictionary to map unit symbols to unit classes for SurfaceArea_SA
units_dict_ma = {R(r'mgPt', group=0): AmperePerMilligramPt}
SurfaceArea_SA.units_dict = units_dict_ma
SurfaceArea_SA.standard_units = AmperePerMilligramPt()