from RGrammar import *

s = "25 + ( 2 + 33 * 45) * 4"
parser = T_EXPRESSION.newParser(s)
# parser.error('TEST ERROR THROWING')
parser.parse()

print str(parser)