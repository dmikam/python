from TParser import *

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
