# -*- coding: utf-8 -*-
"""
Units and models for mass activity.

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


class MassActivity(Dimension):
    """
    Dimension subclass for mass activity.
    """
    pass

class MassActivityModel(QuantityModel):
    """
    Model for mass activity.
    """
    dimensions = MassActivity()

class MassActivityUnit(Unit):
    """
    Base class for units with dimensions of mass activity.
    The standard value for mass activity is defined to be A/mgPt, implemented in the AmperePerMilligramPt class.
    """

    def __init__(self, magnitude=0.0, powers=None):
        super(MassActivityUnit, self).__init__(MassActivity(), magnitude, powers)

class AmperePerMilligramPt(MassActivityUnit):
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

# Dictionary to map unit symbols to unit classes for mass activity
#units_dict_ma = {R(r'A\s*mgPt\s*\^-1', group=0): AmperePerMilligramPt}
units_dict_ma = {R(r'mgPt', group=0): AmperePerMilligramPt}
MassActivity.units_dict = units_dict_ma
MassActivity.standard_units = AmperePerMilligramPt()