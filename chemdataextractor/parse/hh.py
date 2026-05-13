import re
from ..parse import R, I, W, Optional, merge, join
#from ..model import Compound
from ..model.model import Compound, HeinHtet
from .common import hyphen

prefix = (I(u'mass') + I(u'activity') + (W(u'increased')+W(u'to') | Optional(I(u'of')))).hide()
units = ((R('[mA|A]'))+(R('[mg|mgPt]−1')))(u'units').add_action(join)
value = (Optional(R('^[~∼\<\>]$')) + Optional(R('^[\-–−]$')) + R('^[\+\-–−]?\d+(\.\d+)?$'))('value').add_action(merge)
#bp = (value + units)(u'bp')
bp = (prefix + value + units)(u'bp')

from ..parse.base import BaseSentenceParser, BaseParser
from ..utils import first
from lxml import etree

class HHParser(BaseParser):
    root = bp

    def interpret(self, result, start, end):
        compound = Compound(
            hein_htets=[
                HeinHtet(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound