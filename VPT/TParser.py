from TGrammar import *

class TParser(object):
	def __init__(self,grammar,input):
		self.grammar	= TGrammar(grammar)
		self.input		= input
		self.inputIter	= iter(self.input)
		self.stack		= []

	def nextChar(self):
		try:
			return self.inputIter.next()
		except StopIteration:
			return None

	def stackPush(self,newVal):
		self.stack.append(newVal)



	def convertSymbol(self,symbol):
		for rule in self.grammar:
			if type(rule.value) is str and type(symbol) is str and rule.value==symbol:
				return L(rule.name)
			# elif type(rule.value) is tuple and

	def parse(self):
		ch = self.nextChar()
		while ch!=None:
			print ch
			ch = self.nextChar()
			symbol = ch
			while symbol!=None:
				if self.stackPush(ch):
					break;
				else:
					symbol = self.convertSymbol(symbol)

		print "FIN"