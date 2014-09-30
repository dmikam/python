from TParser import *
from RGrammar import *
from TLiteral import *

text = "NUM:DIGIT|NUM   DIGIT;"
# text = "   "

parser = TParser(GRAMMAR,text)
parser.parse()
parser.stackPrint()