# Configurable compiler
This project contains a structure that allows for a verbose definition of a programming language.
This should be used as a bootstrapping compiler, as it is not meant to be efficient, but rather
easy to use for prototyping a new programming language.

This compiler should also be able to output lists of available tokens for the language, and the
grammar of the language in multiple different formats that can be fed into other tools, such as
yacc/bison and flex/lex.


## Components
This system is comprised of multiple components each responsible for a different discreet step of
compilation

### tokens
This module is where any language tokens should be defined.
The order that the lexer tries to parse tokens in is determined by the order of the elements in
the '__all__' export of the tokens module. Each token defined in that array should be decorated with
a '@Token()' decorator, with a appropriate regex passed as an argument to the decorator.
**TODO** Go into greater detail here about how to add a new token and add values to it

### writer
This module is responsible for turning a valid program model into final transpiled code.
The output code can be in any language that is desired
**TODO** describe best practices for the writer

## validation
This module should validate the model of the parsed syntax tree to ensure it is valid for writing.
**TODO** describe validation patterns

## model
This module should represent the shape of the parsed source code, including where in the source the
definitions of the parsed information are to allow for better error reporting