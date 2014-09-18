class TParser(object):
	skipSymbols = ' \t'
	validSymbols = ''

	def __init__(self, stringIter):
		self.iter = stringIter
		self.type = 'PARSER'
		self.val = ''		# Accumulative value from chars from the tape
		self.stack = []

	@staticmethod
	def makeStringIter(s):
		for ch in s:
			yield ch

	@classmethod
	def newParser(CLASS,s):
		iter = CLASS.makeStringIter(s)
		return CLASS(iter)

	def next(self):
		return next(self.iter,None)

	@classmethod
	def getParsers(CLASS):
		return TParser.__subclasses__()

	@classmethod
	def name(CLASS):
		return CLASS.__name__

	@classmethod
	def detect(CLASS):
		for parser in CLASS.getParsers():
			parser

	@classmethod
	def error(CLASS,text):
		raise Exception(CLASS.name() + ': ' + text)

	def skipSymbol(self,ch):
		return ch in self.skipSymbols

	def validSymbol(self,ch):
		return ch in self.validSymbols

	"""
		Checks if the string is valid for this type of object.
		For example:
			- "23.4.5" isn't valid number,
			- "func(tion(" is not valid function
	"""
	def valid(self,value):
		return True

	def parse(self):
		stop = False
		while not stop:
			ch = self.next()
			if not ch:
				break

			if self.skipSymbol(ch):
				continue
			print ch

			if self.validSymbol(ch) and self.valid(self.val + ch):
				self.val += ch
			else:
				self.defect()


class T_EXP(TParser):
	def __init__(self, arg):
		super(TEXP, self).__init__()
		self.arg = arg

s = "25 * ( 2 + 3 * 5)"
parser = TParser.newParser(s)
# parser.error('TEST ERROR THROWING')
parser.parse()

print parser.val