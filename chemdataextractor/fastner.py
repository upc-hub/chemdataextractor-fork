# -*- coding: utf-8 -*-
"""
Configuration for making ChemDataExtractor revert to legacy versions of NER and tokenisation.
This is also much faster than the current NER when run on CPU.

:codeauthor: Taketomo Isazawa (ti250@cam.ac.uk)
"""

from ..doc.text import Text, Sentence
from ..nlp.tokenize import ChemWordTokenizer
from ..nlp.cem import LegacyCemTagger
from ..nlp.pos import ChemCrfPosTagger

Text.taggers = [ChemCrfPosTagger(), LegacyCemTagger()]
Text.word_tokenizer = ChemWordTokenizer()
Sentence.taggers = [ChemCrfPosTagger(), LegacyCemTagger()]
Sentence.word_tokenizer = ChemWordTokenizer()
