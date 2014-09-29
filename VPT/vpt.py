from TParser import *
from RGrammar import *
from TLiteral import *



# parser = TParser(GRAMMAR,'Dima')
# parser.parse()






symbol = TLiteral('D')
tests = [
	'A',
	'D',
	'Dima',
	TLiteral('D'),
	TRule('D',[]),
	['D','A'],
	['A','D'],
	['A','A'],
	['A',['B',TLiteral('D')]],
	('D','A'),
	('A','D'),
	('A','A'),
]

"""
	== 1 - equal
	== 0 - undefined, probably equal
	==-1 - not equal
"""
def makeTest(item,highstack,prefix=''):
	if prefix != '':
		print prefix,str(item),'??',str(highstack)
	else:
		print str(item),'??',str(highstack)
	prefix += '    |'
	if item==highstack:
		res = 1
	elif type(highstack) is list and not type(item) is list:
		res = -1
		for highstackItem in highstack:
			res = makeTest(item,highstackItem,prefix)
			if res>=0:
				break
	else:
		res = -1

	if prefix != '':
		print prefix,res
	else:
		print res

	return res



for test in tests:
	makeTest(symbol,test)