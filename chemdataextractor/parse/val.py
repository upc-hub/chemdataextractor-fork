import re
from ..parse import R, I, W, Optional, merge, join
#from ..model import Compound
from .common import hyphen

#prefix = (I(u'power') + I(u'density') + Optional(I(u'of')) | I(u'density')+ I(u'of')+ I(u'power')).hide()
units = ((R('[w|W|mW|V|m2|mA|A]'))+Optional(R('[m−2|cm−2|g−1]'))+Optional(R('[mg|mgPt]−1')))(u'units').add_action(join)
value = (Optional(R('^[~∼\<\>\+]$')) + Optional(R('^[\-–−]$')) + R('^[\+\-–−]?\d+(\.\d+)?$'))('value').add_action(merge)
bp = (value + units)(u'bp')
#bp = (prefix + value + units)(u'bp')

from ..parse.base import BaseSentenceParser
from ..utils import first
from lxml import etree

class ValueUnitParser(BaseSentenceParser):
    root = bp

    def interpret(self, result, start, end):
        compound = self.model.fields['compound'].model_class()
        raw_value = first(result.xpath('./value/text()'))
        raw_units = first(result.xpath('./units/text()'))
        value_unit = self.model(raw_value=raw_value,
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
        value_unit.compound = compound
        yield value_unit