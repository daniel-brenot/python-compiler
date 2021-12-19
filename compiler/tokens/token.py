import re



class Token(object):
    """
    Decorator for a token to easily set its
    regex for matching when lexing occurs
    """

    def __init__(self, pattern: str):
        self.regex = re.compile(pattern)

    def __call__(self, f):
        f.regex = self.regex
        return f

