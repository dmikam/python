class TParser(object):
	skipSymbols = ''
	validSymbols = ''
	stopOnInvalid = False

	def __init__(self, stringIter):
		self.iter = stringIter
		self.type = 'PARSER'
		self.val = ''		# Accumulative value from chars from the tape
		self.stack = []
	# /__init__

	def __str__(self):
		print self.name()

	@staticmethod
	def makeStringIter(s):
		for ch in s:
			yield ch
	# /makeStringIter

	@classmethod
	def newParser(CLASS,s):
		iter = CLASS.makeStringIter(s)
		return CLASS(iter)
	# /newParser

	def next(self):
		return next(self.iter,None)
	# /next

	@classmethod
	def getParsers(CLASS):
		return TParser.__subclasses__()
	# /getParsers

	@classmethod
	def name(CLASS):
		return CLASS.__name__
	# /name

	@classmethod
	def error(CLASS,text):
		raise Exception(CLASS.name() + ': ' + text)
	# /error

	def skipSymbol(self,ch):
		return ch in self.skipSymbols
	# /skipSymbol

	@classmethod
	def validSymbol(CLASS,ch):
		return ch in CLASS.validSymbols
	# /validSymbol

	"""
		Checks if the string is valid for this type of object.
		For example:
			- "23.4.5" isn't valid number,
			- "func(tion(" is not valid function
	"""
	@classmethod
	def valid(CLASS,value):
		# Conditions to check
		return True
	# /valid

	@classmethod
	def detect(CLASS,ch):
		parserCandidats = []
		for parser in CLASS.getParsers():
			if parser.validSymbol(ch) and parser.valid(ch):
				parserCandidats.append(parser)
		# /for

		return parserCandidats
	# /detect

	def parse(self):
		stop = False
		print self.name()
		while not stop:
			ch = self.next()

			# if input end reached
			if ch==None:
				break

			if self.skipSymbol(ch):
				continue
			print ch

			if self.validSymbol(ch) and self.valid(self.val + ch):
				self.val += ch
			else:
				if self.stopOnInvalid:
					stop = True
					continue


				# parse subsequent expressions
				parserCandidats = self.detect(ch)
				if len(parserCandidats):
					# just for now, we'll use only the first found candidate
					parser = parserCandidats[0](self.iter)
					self.stack.append(parser.parse())
					# print parser
				else:
					self.error('Unexpected symbol "{}" found in {}'.format(ch,self.name()))
			# /else
		# /while

		return self
	# /parse

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

s = "25 * ( 2 + 3 * 5)"
parser = TParser.newParser(s)
# parser.error('TEST ERROR THROWING')
parser.parse()

print parser.stack