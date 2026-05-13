from cde_n.chemdataextractor.parse.base import BaseSentenceParser
from cde_n.chemdataextractor.utils import first
from cde_n.chemdataextractor.parse import R, I, W, Optional, merge, join
from cde_n.chemdataextractor.model.model import Compound

prefix = (I(u'bbb')|I(u'aaa')).hide()
units = ((R('[A|mA]'))+(R('[mgPt−1|cm−2]')))(u'units').add_action(join)
value = (Optional(R('^[~∼\<\>]$')) + Optional(R('^[\-–−]$')) + R('^[\+\-–−]?\d+(\.\d+)?$'))('value').add_action(merge)
new_property = (prefix + value + units)(u'new_property')


class testcdParser(BaseSentenceParser):
    root = new_property

    def interpret(self, result, start, end):
        raw_value = first(result.xpath('./value/text()'))
        raw_units = first(result.xpath('./units/text()'))
        created_property = self.model(raw_value=raw_value,
                    raw_units=raw_units,
                    value=self.extract_value(raw_value),
                    error=self.extract_error(raw_value),
                    )
        cem_el = first(result.xpath('./cem'))
        if cem_el is not None:
            created_property.compound = Compound()
            created_property.compound.names = cem_el.xpath('./name/text()')
            created_property.compound.labels = cem_el.xpath('./label/text()')
        yield created_property
