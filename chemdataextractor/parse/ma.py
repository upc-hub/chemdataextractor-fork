import re
from ..parse import R, I, W, Optional, merge, join
#from ..model import Compound
from .common import hyphen

prefix = (I(u'mass') + I(u'activity') + (W(u'increased')+W(u'to') | Optional(I(u'of')))).hide()
units = ((R('[mA|A]'))+(R('[mg|mgPt]−1')))(u'units').add_action(join)
value = (Optional(R('^[~∼\<\>]$')) + Optional(R('^[\-–−]$')) + R('^[\+\-–−]?\d+(\.\d+)?$'))('value').add_action(merge)
#bp = (value + units)(u'bp')
bp = (prefix + value + units)(u'bp')

from ..parse.base import BaseSentenceParser
from ..utils import first
from lxml import etree

class MassActivityParser(BaseSentenceParser):
    root = bp

    def interpret(self, result, start, end):
        compound = self.model.fields['compound'].model_class()
        raw_value = first(result.xpath('./value/text()'))
        raw_units = first(result.xpath('./units/text()'))
        current = self.model(raw_value=raw_value,
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
        current.compound = compound
        yield current