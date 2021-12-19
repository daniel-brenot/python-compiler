from .token import Token


@Token(r'\:')
class ColonToken:
    pass

@Token(r'\,')
class CommaToken:
    pass

@Token(r'\.')
class DotToken:
    pass

@Token(r'\(')
class LeftParenToken:
    pass

@Token(r'\)')
class RightParenToken:
    pass

@Token(r'\[')
class LeftBracketToken:
    pass

@Token(r'\]')
class RightBracketToken:
    pass

@Token(r'\<')
class LeftArrowToken:
    pass

@Token(r'\>')
class RightArrowToken:
    pass



