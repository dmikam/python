class TGrammar(object):
	def __init__(self,grammar_description):
		if type(grammar_description) is list:
			self.rules = grammar_description


	def __iter__(self):
		return (rule for rule in self.rules)

	def findRule(self,literal,stack=[]):
		for r in self.rules:
			if r.name=='':
				return r
