from TParser import *

DICT = [
	R('DIGIT',	[
		'0','1','2','3','4','5','6','7','8','9'
	]),
	R('LETTER',	[
		'_',
		'a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
		'A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
	]),
	R('NAME',		[
		L('LETTER'),
		(
			L('NAME'),
			L('LETTER')
		),
		(
			L('NAME'),
			L('DIGIT')
		)
	]),
	R('SNG_STRING', (
		# REGEXP('/"[^"\\\\]*(?:\\\\.[^"\\\\]*)*"/s')
		"'",
		REGEXP(r'((\\"|[^"])*)'),
		"'"
	)),
	R('DBL_STRING', (
		# REGEXP("/'[^'\\\\]*(?:\\\\.[^'\\\\]*)*'/s")
		'"',
		REGEXP(r"((\\'|[^'])*)"),
		'"'
	)),
	R('STRING',	[
		L('SNG_STRING'),
		L('DBL_STRING')
	]),
	# R('RULE', [
	# 	[]
	# ])
];


