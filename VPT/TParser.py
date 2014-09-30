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
			symbol = self.convertSymbol(tuple(newStack[i:]))
			if symbol!=None:
				print str(self.stack),'<==',str(symbol)
				self.stack.append(symbol)
				print str(self.stack)
				return True

		return False

	def stackInspect(self):
		print "------------------------------------------------------------------------"
		print "                            STACK INSPECT                               "
		print "------------------------------------------------------------------------"
		while True:
			noChanges = True
			for i in xrange(len(self.stack)):
				symbol = self.convertSymbol(tuple(self.stack[i:]))
				if symbol!=None:
					oldStack = self.stack[:]
					self.stack = self.stack[:i]
					self.stack.append(symbol)
					print '----------------------------------'
					print oldStack,'==>',self.stack
					print '----------------------------------'
					noChanges = False

			break
			# if noChanges:
			# 	break

	def stackInspectFromHead(self):
		print "------------------------------------------------------------------------"
		print "                            STACK INSPECT                               "
		print "------------------------------------------------------------------------"
		i=0
		while True:
			if i>len(self.stack)-2:
				break

			symbol = self.convertSymbol((self.stack[i],self.stack[i+1]))
			print (self.stack[i],self.stack[i+1]),'-->',symbol

			if symbol==None:
				print '[[[[[[[[[[[[[i++]]]]]]]]]]]]]'
				print i,'>',len(self.stack)-2
				i += 1
				if i<len(self.stack)-2:
					continue
			else:
				oldStack = self.stack[:]
				newStack = self.stack[:i]
				newStack.append(symbol)
				newStack.extend(oldStack[i+2:])
				self.stack = newStack
				print '----------------------------------'
				print oldStack,'==>',self.stack
				print '----------------------------------'

	def stackPrint(self):
		for item in self.stack:
			print item.result()


	def convertSymbol(self,symbol):
		for rule in self.grammar:
			if rule.test(symbol)>0:
				literal = TLiteral(rule.name,symbol)
				literal.pack()
				return literal

		return None


	def parse(self):
		ch = self.nextChar()
		while ch!=None:
			print "'" + str(ch) + "'"
			literal = ch


			self.stackPush(literal)
			self.stackInspect()

			ch = self.nextChar()

		# self.stackInspectFromHead()

		print "FIN"