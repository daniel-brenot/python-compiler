"""
This file handles taking an input of source code and outputting tokens
"""

from typing import AnyStr, Pattern, List
from compiler.tokens import __all__ as token_list
import compiler.tokens

def tokenize(input: str) -> List[object]:
    tokens = []
    while len(input) > 0:
        for token_name in token_list:
            regex = getattr(compiler.tokens, token_name).regex
            match = regex.match(input)
            if match:
                match_value = match.group(0)
                token = getattr(compiler.tokens, token_name)().parse(match_value)
                input = input[len(match_value):]
                tokens.append()
                break

