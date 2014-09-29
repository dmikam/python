from TParser import *
from RGrammar import *
from TLiteral import *

prefix = ''


parser = TParser(GRAMMAR,'Walking dead are alive ()')
parser.parse()
parser.stackPrint()