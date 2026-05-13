# -*- coding: utf-8 -*-
"""
Units and models for testcd.

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


class testcd(Dimension):
    """
    Dimension subclass for testcd.
    """
    pass

class testcdModel(QuantityModel):
    """
    Model for testcd.
    """
    dimensions = testcd()

class testcdUnit(Unit):
    """
    Base class for units with dimensions of testcd.
    The standard value for testcd is defined to be A/mgPt, implemented in the AmperePerMilligramPt class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(testcdUnit, self).__init__(testcd(), magnitude, powers)

class AmperePerMilligramPt(testcdUnit):
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

# Dictionary to map unit symbols to unit classes for testcd
units_dict_ma = {R(r'mgPt', group=0): AmperePerMilligramPt}
testcd.units_dict = units_dict_ma
testcd.standard_units = AmperePerMilligramPt()