# -*- coding: utf-8 -*-
"""
Units and models for PowerTest.

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


class PowerTest(Dimension):
    """
    Dimension subclass for PowerTest.
    """
    pass

class PowerTestModel(QuantityModel):
    """
    Model for PowerTest.
    """
    dimensions = PowerTest()

class PowerTestUnit(Unit):
    """
    Base class for units with dimensions of PowerTest.
    The standard value for PowerTest is defined to be A/mgPt, implemented in the AmperePerMilligramPt class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(PowerTestUnit, self).__init__(PowerTest(), magnitude, powers)

class AmperePerMilligramPt(PowerTestUnit):
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

# Dictionary to map unit symbols to unit classes for PowerTest
units_dict_ma = {R(r'mgPt', group=0): AmperePerMilligramPt}
PowerTest.units_dict = units_dict_ma
PowerTest.standard_units = AmperePerMilligramPt()