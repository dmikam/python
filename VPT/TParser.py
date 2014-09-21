import re


class TParser(object):
	def __init__(self, stringIter, dict):
		self.iter = stringIter
		self.val = ''		# Accumulative value from chars from the tape
		self.stack = TStack()
		self.dict = dict
	# /__init__

	def __str__(self,prefix=''):
		s = prefix + self.name() + '('+str(self.val)+')' + '\n'
		if len(self.stack)>0:
			prefix += '    '
			s += prefix + '|\n'
			for sub in self.stack:
				s += sub.__str__(prefix)

		return s

	# /str

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

	def checkRule(self,rule,buf,INDENT=''):
		INDENT += '    '
		ruleType	= type(rule)
		# print ruleType
		# list = OR
		if ruleType is list:
			print INDENT,"\\ list",buf,'==',rule
			result = False
			for ruleItem in rule:
				print INDENT,"\\ listItem",buf,'==',ruleItem
				result = result or self.checkRule(ruleItem,buf,INDENT)
				if result:
					break
			print INDENT,result
			return result
		# tuple = AND
		elif ruleType is tuple:
			print INDENT,"\\ tuple",buf,'==',rule
			result = True
			for ruleItem in rule:
				print "\\ tupleItem",buf,'==',ruleItem
				result = result and self.checkRule(ruleItem,buf,INDENT)
				if not result:
					break
			print INDENT,result
			return result
		elif ruleType is str:
			print INDENT,"\\ str",buf,'==',rule
			result = rule==buf
			print INDENT,result
			return result
		elif ruleType is REGEXP:
			print INDENT,"\\ regexp",buf,'==',rule
			result = rule.check(buf)
			print INDENT,result
			return result
		elif rule is L:
			print "? L",buf,'==',rule.name
			return buf is L and buf.name==rule.name
			# return self.checkRule(self.dict[rule.name],buf)
		else:
			print INDENT,"???????????????????????????????????"
			print INDENT,ruleType,rule
			print INDENT,"???????????????????????????????????"
		return False


	def parse(self):
		stop = False

		buf = BUF('','')
		while not stop:
			ch = self.next()
			print ch
			# if input end reached
			if ch==None:
				self.stack.push(buf)
				break


			if buf.name!='':
				print "Continue with the same buf"
				if self.checkRule(self.dict[buf.ruleIndex].rule,buf.val+ch):
					buf.val		+= ch
				else:
					self.stack.push(buf)
					buf = BUF('','')

			if buf.name=='':
				for ruleIndex,rule in enumerate(self.dict):
					print "\\",rule.name
					if self.checkRule(rule.rule,buf.val+ch):
						print rule.name
						buf.ruleIndex	= ruleIndex
						buf.name		= rule.name
						buf.val		   += ch
						break
				else:
					self.error('Unexpected symbol "{}"'.format(ch))


			print buf
			print self.stack

			print "CHECKING STACK"
			for ruleIndex,rule in enumerate(self.dict):
				print "\\",rule.name
				if self.checkRule(rule,self.stack):
					print rule.name
					buf.ruleIndex	= ruleIndex
					buf.name		= rule.name
					buf.val		   += ch
					break

		# /while

		return self
	# /parse
# /class TParser

class L(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name


class BUF(object):
	def __init__(self,name,val):
		self.name		= name
		self.val		= val
		self.ruleIndex	= None

	def __str__(self):
		return 'BUF(' + self.name + ': ' + self.val + ')'
	def __repr__(self):
		return 'BUF(' + self.name + ': ' + self.val + ')'




class REGEXP(object):
	def __init__(self, exp):
		self.exp = exp
		self.re = re.compile(exp)

	def check(self,s):
		M = self.re.match(s)
		G = M.groups()
		if len(G)>0 and len(G[0])==len(s):
			return True
		else:
			return False



class R(object):
	def __init__(self,name,rule):
		self.name	= name
		self.rule	= rule

	def prototype(self,rule=None):
		root = False
		if rule==None:
			rule = self.rule
			root = True

		protoArray = []
		for rItem in self.rule:
			rItemType = type(rItem)
			if rItemType is L:
				if root:
					protoArray.append('(' + rItem.name + ')')
				else:
					protoArray.append(rItem.name)
			elif rItemType is str:
				protoArray.append("'" + rItem + "'")
			elif rItemType is REGEXP:
				protoArray.append("REGEXP")
			else:
				protoArray.append(str(rItem))
				# protoArray.append(self.prototype(rItem))

		proto = ' '.join(protoArray)
		if type(self.rule) is list:
			proto = '[' + proto + ']'
		elif type(self.rule) is tuple:
			proto = '(' + proto + ')'

		return proto


class TStack(object):
	def __init__(self,content=[]):
		self.content = content

	def push(self,val):
		self.content.append(val)

	def pop(self):
		return self.content.pop()

	def __repr__(self):
		return 'STACK' + str(self.content)

	def checkRule(self,rule):
		# if len(self.content)>len(rule):
		# 	return -1

		equal = True
		for sIndex,sItem in enumerate(self.content):
			print sIndex,sItem

			continue
			if type(sItem) == type(rItem) and sItem==rItem:
				equal = True
				continue

			if type(sItem) is BUF and type(rItem) is L:
				print sItem.name, rItem.name
				if sItem.name==rItem.name:
					equal = True
					continue
			equal = False
		# /for

		if equal and len(self.content)==len(rule):
			return 0
		elif equal and len(self.content)<len(rule):
			return 1


		return -1

	def prototype(self):
		protoArray = []
		for sItem in self.content:
			sItemType = type(sItem)
			if sItemType is BUF:
				protoArray.append(sItem.name)
			elif sItemType is str:
				protoArray.append("'" + sItem + "'")

		proto = ' '.join(protoArray)
		proto = '(' + proto + ')'

		return proto
