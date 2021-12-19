import inspect
import types
import sys
from typing import Type, get_type_hints


def parse(context: Type[object]):
    """Takes in an initial class that has all of the grammars under it and parses all productions"""

    def sort_key(item):
        return inspect.findsource(getattr(context, item))[1]

    # List of properties in order of definition
    properties = [
        attribute for attribute in dir(context)
        if callable(getattr(context, attribute)) and attribute.startswith('_') is False
    ]
    properties.sort(key=sort_key)

    # A list of sorted productions and their required types
    productions = [
        (attribute, get_type_hints(getattr(context, attribute)).values()) for attribute in properties
    ]

    print(productions)
    
