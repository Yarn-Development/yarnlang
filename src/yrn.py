from lexer import Lexer
from parser import Parser
def run(fn,text):
    lexer = Lexer(fn,text)
    tokens, error = lexer.make_tokens()
    if error: return None,error
    #Gen AST
    parser = Parser(tokens)
    ast = parser.parse()
    return ast.node, ast.error
