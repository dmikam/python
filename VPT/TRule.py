from TLiteral import *
prefix = ''

class TRule(TLiteral):
	def __init__(self,name,value):
		super(self.__class__,self).__init__(name,value)


	def test(self,item):
		return self.ruleTest(item,self.value)

	"""
		== 1 - equal
		== 0 - undefined, probably equal
		==-1 - not equal
	"""
	@classmethod
	def ruleTest(cl,item,highstack):
		global prefix

		res = -1

		print prefix + str(item) + ' ?? ' + str(highstack)
		oldPrefix = prefix
		prefix += '    |'

		if item==highstack:
			res = 1
		elif type(highstack) is list and not type(item) is list:
			res = -1
			for highstackItem in highstack:
				res = cl.ruleTest(item,highstackItem)
				if res>=0:
					break
		elif type(highstack) is tuple and not type(item) is tuple:
			if cl.ruleTest(item,highstack[0])>=0:
				res = 0 # undefined, probably equal
		elif type(highstack) is tuple and type(item) is tuple and len(item)<len(highstack):
			res = 0
			for i in xrange(len(item)):
				if cl.ruleTest(item[i],highstack[i])<0:
					res = -1 # undefined, probably equal
					break

		prefix = oldPrefix
		print prefix + str(res)

		return res
