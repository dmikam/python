class TName:
	def __init__(self, val=''):
		self.val = val

	def push(char):
		self.val += char



class TIterator:
	@classmethod
	def getLines(cl,input):
		lines = input.split('\n')
		for line in lines:
			yield line.strip()

	@classmethod
	def getChars(cl,input):
		for char in input:
			yield char

	@classmethod
	def getDefinitions(cl,input):
		lineIter = cl.getLines(input)
		definition = line = lineIter.next()
		while line:
			while (definition[-1]!=';'):
				definition = ' '.join((definition, lineIter.next()))
			(var,symbstring) = definition.split(':',1)

			if symbstring[-1]==';':
				symbstring = symbstring[:-1]

			yield (var,symbstring.strip())
			definition = line = lineIter.next()
		# /while
	# /getDefinitionIterator

	@classmethod
	def getTokens(cl,input):
		charsIter = cl.detChars(input)
		string = False
		ch = charsIter.next()
		while ch:

			ch = charsIter.next()


class TGrammar(TIterator):
	def __init__(self, input=''):
		self.input = input

	def loadFromFile(self,filename):
		f = open(filename,'r')
		self.input = f.read()


	def parse(self):
		defIter = TIterator.getDefinitions(self.input)

		for definition in defIter:
			print str(definition) + "\n=======================\n"



g = TGrammar()
g.loadFromFile('test_grammar.gr')
g.parse()
