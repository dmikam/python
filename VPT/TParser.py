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

		for i in xrange(len(newStack)):
			print 'i=',i
			symbol = self.convertSymbol(tuple(newStack[i:]))
			if symbol!=None:
				self.stack.append(symbol)
				return True

		return False

	def stackInspect(self):
		print "------------------------------------------------------------------------"
		print "                            STACK INSPECT                               "
		print "------------------------------------------------------------------------"
		while True:
			noChanges = True
			for i in xrange(len(self.stack)):
				print 'i=',i
				symbol = self.convertSymbol(tuple(self.stack[i:]))
				if symbol!=None:
					self.stack = self.stack[:i]
					self.stack.append(symbol)
					noChanges = False

			if noChanges:
				break


	def convertSymbol(self,symbol):
		for rule in self.grammar:
			if rule.test(symbol)>0:
				return TLiteral(rule.name,symbol)

		return None


	def parse(self):
		ch = self.nextChar()
		while ch!=None:
			print "'" + str(ch) + "'"
			literal = ch


			self.stackPush(literal)
			self.stackInspect()
			print "------------------------------------------------------------------------"
			print "=====>STACK: ",str(self.stack)
			print "------------------------------------------------------------------------"

			ch = self.nextChar()

		print "FIN"