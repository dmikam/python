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

		# print prefix + str(item) + ' ?? ' + str(highstack)

		oldPrefix = prefix
		prefix += '    |'

		if item==highstack:
			# print 'CASE 1:',item,'==',highstack
			res = 1
		elif type(highstack) is list and not type(item) is list:
			# print 'CASE 2:',item,'->',highstack
			res = -1
			for i,highstackItem in enumerate(highstack):
				# print '-------->',i
				res = cl.ruleTest(item,highstackItem)
				if res>0:
					break
		elif type(highstack) is tuple and not type(item) is tuple:
			# print 'CASE 3:',item,'->',highstack
			if cl.ruleTest(item,highstack[0])>=0:
				res = 0 # undefined, probably equal
		elif type(highstack) is tuple and type(item) is tuple and len(item)<=len(highstack):
			# print 'CASE 4:',item,'<==>',highstack
			res = 0
			matches = 0
			for i in xrange(len(item)):
				if cl.ruleTest(item[i],highstack[i])>=0:
					matches += 1
				else:
					res = -1
					break
			if res==0 and matches==len(highstack):
				res = 1
		elif type(item) is tuple and not type(highstack) is tuple:
			# print 'CASE 5:',item,'<-->',highstack
			# print tuple(item),'!!',tuple(highstack),tuple(item)==tuple(highstack)
			res = cl.ruleTest(item,tuple([highstack]))
		# else:
			# print 'CASE 6:',item,'!!',highstack
			# print type(item),type(highstack)


		prefix = oldPrefix
		# print prefix + str(res)

		return res
