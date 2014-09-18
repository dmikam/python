class TParser:
	tEXP	= 'EXP'
	tNUM	= 'NUM'
	tOP		= 'OP'

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
	def newParser(selfClass,s):
		iter = selfClass.makeStringIter(s)
		return selfClass(iter)

	def next(self):
		return self.iter.next()

	def parse(self):
		stop = False
		while not stop:
			ch = self.next()


class T_EXP(TParser):
	def __init__(self, arg):
		super(TEXP, self).__init__()
		self.arg = arg

s = "Hello World"
parser = TParser.newParser(s)

for ch in parser.iter:
	print ch