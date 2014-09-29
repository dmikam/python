from TGrammar import *
from TLiteral import *

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
		print "------------------------------------------------------------------------"
		print "                            PUSH TO STACK                               "
		print "------------------------------------------------------------------------"
		newStack = self.stack[:]
		newStack.append(newVal)
		symbol = self.convertSymbol(tuple(newStack))
		if symbol!=None:
			self.stack.append(symbol)
			return True

		return False


	def convertSymbol(self,symbol):
		for rule in self.grammar:
			if rule.test(symbol)>0:
			# if rule.test(symbol)>=0:
				return TLiteral(rule.name,symbol)

		return None


	def parse(self):
		ch = self.nextChar()
		while ch!=None:
			print "'" + str(ch) + "'"
			literal = ch
			while literal!=None:
				print str(literal)
				if self.stackPush(literal):
					print "------------------------------------------------------------------------"
					print "=====>STACK: ",str(self.stack)
					print "------------------------------------------------------------------------"
					break;
				else:
					print "------------------------------------------------------------------------"
					print "                           CONVERT SYMBOL                               "
					print "------------------------------------------------------------------------"
					literal = self.convertSymbol(literal)
					print "!!!!!!!!", literal

			ch = self.nextChar()

		print "FIN"