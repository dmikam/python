from TLiteral import *

class TRegexp(TLiteral):
	def __init__(self,rule,value=None):
		super(self.__class__,self).__init__('REGEXP',value)
		self.rule = rule