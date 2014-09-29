class TLiteral(object):
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return self.__class__.__name__+'('+self.name+')'

	def __repr__(self):
		return str(self)

	def __eq__(self,other):
		# print '    |'
		# print '    ',other.__class__,self.__class__,isinstance(other,self.__class__)#, self.name, other.name, isinstance(other,self.__class__) and self.name==other.name
		if (isinstance(other,self.__class__) or isinstance(self,other.__class__)) and self.name==other.name:
			print str(self) + '==' + str(other)
			return True
		else:
			print str(self) + '!=' + str(other)
			return False
