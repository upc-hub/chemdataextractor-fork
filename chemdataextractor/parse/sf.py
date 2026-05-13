import re
from ..parse import R, I, W, Optional, merge, join
#from ..model import Compound
from .common import hyphen

prefix = (I(u'surface') + I(u'area') + Optional(I(u'of')) | I(u'area')+ I(u'of')+ I(u'surface')).hide()
units = ((R('[m2]'))+(R('[g−1]')))(u'units').add_action(join)
value = (Optional(R('^[~∼\<\>]$')) + Optional(R('^[\-–−]$')) + R('^[\+\-–−]?\d+(\.\d+)?$'))('value').add_action(merge)
bp = (prefix + value + units)(u'bp')
#bp = (value + units)(u'bp')

from ..parse.base import BaseSentenceParser
from ..utils import first
from lxml import etree

class SurfaceAreaParser(BaseSentenceParser):
    root = bp

    def interpret(self, result, start, end):
        compound = self.model.fields['compound'].model_class()
        raw_value = first(result.xpath('./value/text()'))
        raw_units = first(result.xpath('./units/text()'))
        surface = self.model(raw_value=raw_value,
                    raw_units=raw_units)
        
        #melting_point = self.model(raw_value=raw_value,
        #            raw_units=raw_units,
        #            value=self.extract_value(raw_value),
        #            error=self.extract_error(raw_value),
        #            units=self.extract_units(raw_units, strict=True))
        #cem_el = first(result.xpath('./cem'))
        #if cem_el is not None:
        #    current.compound = Compound()
        #    current.compound.names = cem_el.xpath('./name/text()')
        #    current.compound.labels = cem_el.xpath('./label/text()')
        surface.compound = compound
        yield surface