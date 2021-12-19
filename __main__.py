
from compiler.lexing.lexer import tokenize



class OtherNonterminal:

    value = ''

class SomeOtherNonterminal:

    value = ''

class ExampleNonTerminal:

    def example_production2(hello: SomeOtherNonterminal, albert: int, world: str):
        hello.value

    def example_production(hello: OtherNonterminal):
        hello.value

    


if __name__ == "__main__":
    tokenize('12.345class12')