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

	TRule('EOLNCHAR',	[ '\n', '\r' ]),

	TRule('EOLN',	(
		[
			'EOLNCHAR',
			'EOLN'
		],
		'EOLN'
	)),
	TRule('WSPACECHAR',	[
		' ',
		'\t',
	]),
	TRule('WSPACE',	[
		TLiteral('WSPACECHAR'),
		(
			TLiteral('WSPACE'),
			TLiteral('WSPACECHAR')
		)
	]),
	TRule('COLON',':'),
	TRule('SEMICOLON',';'),
	TRule('OR','|'),

	TRule('EXPRESSION',(
		TLiteral('NAME'),
		TLiteral('WSPACE'),
		TLiteral('NAME'),
	)),

	TRule('RULEITEM',[
		(
			[TLiteral('COLON'),TLiteral('OR')],
			TLiteral('NAME'),
		),
		(
			TLiteral('RILEITEM'),
			[
				TLiteral('WSPACE'),
				TLiteral('NAME')
			]
		)
	]),
	# TRule('RULE',[
	# 	(
	# 		TLiteral('NAME'),
	# 		[TLiteral('RULEITEM'), TLiteral('NAME')]
	# 	),
	# 	(
	# 		TLiteral('RULE'),
	# 		[TLiteral('RULEITEM'), TLiteral('NAME')]
	# 	),
	# ]),
]
