from TParser import *


VARS = {
	'LETTER':	[
		'a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
		'A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
	],
	'DIGIT':	[
		'0','1','2','3','4','5','6','7','8','9'
	],
	'NAME':		[
		L('LETTER'),
		[
			L('NAME'),
			L('LETTER')
		],
		[
			L('NAME'),
			L('DIGIT')
		]
	],
	'STRING':	[
		REGEXP('\'[^\']*\'')
	]
}
class T_COLON()
class T_NAME(TParser):
	name = 'T_NAME'
	rules = [
		L('T_LETTER'),
		[
			L('T_NAME'),
			L('T_LETTER')
		]
	]


class T_EXPRESSION(TParser):
	skipSymbols = ' \t'
	validSymbols = ''
	stopOnInvalid = False

class T_NUMBER(TParser):
	skipSymbols = ''
	validSymbols = '0123456789'
	stopOnInvalid = True

class T_OP(TParser):
	skipSymbols = ''
	validSymbols = '*+-/'
	stopOnInvalid = True

class T_BRACKET(TParser):
	skipSymbols = ' \t'
	validSymbols = '()'
	stopOnInvalid = False

	@classmethod
	def valid(CLASS,value):
		if value =='(' or value=='()':
			return True
		else:
			return False
