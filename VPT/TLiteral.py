class TLiteral(object):
	def __init__(self,name,value=None):
		self.name	= name
		self.value	= value

	def __str__(self):
		val = ''
		if self.value!=None:
			val = str(tuple(self.value))
		# return self.__class__.__name__ + '(' + self.name + val + ')'
		return self.name + val

	def __repr__(self):
		return str(self)

	def __eq__(self,other):
		global prefix
		# print '    |'
		# print '    ',other.__class__,self.__class__,isinstance(other,self.__class__)#, self.name, other.name, isinstance(other,self.__class__) and self.name==other.name
		if (isinstance(other,self.__class__) or isinstance(self,other.__class__)) and self.name==other.name:
			print str(self) + ' == ' + str(other)
			return True
		else:
			print str(self) + ' != ' + str(other)
			return False
