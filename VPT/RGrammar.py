from TLiteral import *
from TRule import *
from TRegexp import *

GRAMMAR = [
	TRule('DIGIT',	[
		'0','1','2','3','4','5','6','7','8','9'
	]),
	TRule('LETTER',	[
		'_',
		'a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
		'A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
	]),
	TRule('NAME', (
			[
				TLiteral('LETTER'),
				TLiteral('NAME'),
			],
			[
				TLiteral('LETTER'),
				TLiteral('DIGIT')
			]
	)),
	TRule('SNG_STRING', (
		# TRegexp('/"[^"\\\\]*(?:\\\\.[^"\\\\]*)*"/s')
		"'",
		TRegexp(r'((\\"|[^"])*)'),
		"'"
	)),
	TRule('DBL_STRING', (
		# TRegexp("/'[^'\\\\]*(?:\\\\.[^'\\\\]*)*'/s")
		'"',
		TRegexp(r"((\\'|[^'])*)"),
		'"'
	)),
	TRule('STRING',	[
		TLiteral('SNG_STRING'),
		TLiteral('DBL_STRING')
	]),
	TRule('WSPACECHAR',	[
		' ',
		'\t',
	]),
	TRule('WSPACE',	(
		[
			TLiteral('WSPACECHAR'),
			TLiteral('WSPACE'),
		],
		TLiteral('WSPACECHAR')
	)),
	# TRule('RULE', [
	# 	[]
	# ])
]
