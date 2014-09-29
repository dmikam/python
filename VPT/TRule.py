from TLiteral import *

class TRule(TLiteral):
	def __init__(self,name,value):
		super(self.__class__,self).__init__(name)
		self.value	= value