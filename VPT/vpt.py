from RGrammar import DICT
from TParser import *
import re

# s = "25 + ( 2 + 33 * 45) * 4"
# parser = T_EXPRESSION.newParser(s)
# # parser.error('TEST ERROR THROWING')
# parser.parse()

# print str(parser)

# input = "NUM: DIGIT | NUM DIGIT;\
# DIGIT:	'0'|'1'|'2'|'3'|\
# 		'4'|'5'|'6'|'7'|'8'|'9';\
# "

# input = "Dima"
# strIter = TParser.makeStringIter(input)
# parser = TParser(strIter,DICT)
# parser.parse()
# print parser.stack.prototype()


stack = TStack([
	BUF('LETTER','D'),
	BUF('LETTER','i'),
	BUF('LETTER','m'),
	BUF('LETTER','a')
])

print stack

for rule in DICT:
	print rule.name, stack.checkRule(rule.rule)

# for r in DICT:
# 	print r.name,r.prototype()

# R = REGEXP(r"((\\'|[^'])*)")
# s = "\\'asdas\\'df12\\'"
# r = R.check(s)
# print s
# if r:
# 	print "TRUE"
# else:
# 	print "FALSE"

# r = re.match(r"(\d+)\.?(\d+)?", "24.22333.21")
# print r.groups()
