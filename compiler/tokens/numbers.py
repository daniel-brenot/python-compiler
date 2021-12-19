
from .token import Token

@Token(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)')
class FloatLiteralToken:
    pass

@Token(r'[0-9]+')
class IntegerLiteralToken:
    pass