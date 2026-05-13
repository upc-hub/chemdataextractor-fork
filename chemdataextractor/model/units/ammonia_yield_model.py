# -*- coding: utf-8 -*-
"""
Units and models for ammonia_yield.

.. codeauthor:: Amgad-1 by automatic parser tool

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


class ammonia_yield(Dimension):
    """
    Dimension subclass for ammonia_yield.
    """
    pass

class ammonia_yieldModel(QuantityModel):
    """
    Model for ammonia_yield.
    """
    dimensions = ammonia_yield()

class ammonia_yieldUnit(Unit):
    """
    Base class for units with dimensions of ammonia_yield.
    The standard value for ammonia_yield is defined to be A/mgPt, implemented in the AmperePerMilligramPt class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(ammonia_yieldUnit, self).__init__(ammonia_yield(), magnitude, powers)

class AmperePerMilligramPt(ammonia_yieldUnit):
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

# Dictionary to map unit symbols to unit classes for ammonia_yield
units_dict_ma = {R(r'mgPt', group=0): AmperePerMilligramPt}
ammonia_yield.units_dict = units_dict_ma
ammonia_yield.standard_units = AmperePerMilligramPt()