from lark import Lark
from ast_builder import ASTBuilder
from interpreter import Interpreter

# Load grammar
with open("grammar.lark") as f:
    grammar = f.read()

# Parse input
with open("test_input.txt") as f:
    code = f.read()

parser = Lark(grammar, parser='lalr', start='start')
tree = parser.parse(code)

# Build AST and run
ast = ASTBuilder().transform(tree)
interpreter = Interpreter()
interpreter.execute(ast)
