class TLiteral(object):
	def __init__(self,name,value=None):
		self.name	= name
		self.value	= value
		self.closed	= False

	def close(self):
		self.closed = True

	def isClosed(self):
		return self.closed

	def __str__(self):
		val = ''
		if self.value!=None:
			# val = str(self.value)
			val = str(tuple(self.value))
		# return self.__class__.__name__ + '(' + self.name + val + ')'
		return self.name + val

	def __repr__(self):
		return str(self)

	def __eq__(self,other):
		if (isinstance(other,self.__class__) or isinstance(self,other.__class__)) and self.name==other.name:
			print str(self) + ' == ' + str(other)
			return True
		else:
			# print str(self) + ' != ' + str(other)
			return False

	def pack(self):
		self.value = self.packValue(self.value)

	@classmethod
	def packValue(cl,value):
		if isinstance(value,cl):
			return value.val()
		elif type(value) is str:
			return value
		elif type(value) is tuple or type(value) is list:
			l = []
			for item in value:
				l.append(cl.packValue(item))
			return ''.join(l)

		return value

	def val(self):
		if type(self.value) is str:
			return self.value
		else:
			res = ''
			for item in self.value:
				if type(item) is str:
					res += item
				elif isinstance(item,self.__class__):
					res += item.val()

		return res

	def result(self):
		return self.name + '('+self.val()+')'