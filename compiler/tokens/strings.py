from compiler.tokens.token import Token


@Token(r'\"([^\\\"]|\\.)*\"')
class StringLiteralToken:
    pass