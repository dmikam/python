from TLiteral import *

class TRegexp(TLiteral):
	def __init__(self,rule):
		self.name = 'REGEXP'
		self.rule = rule