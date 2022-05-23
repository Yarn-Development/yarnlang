from tokens import *
from nodes import *
from error import InvalidSyntaxError
class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
    def register(self,result):
        if isinstance(result, ParseResult):
            if result.error: self.error = result.error
            return result.node
        return result
    def success(self,node):
        self.node = node
        return self
    def failiure(self,error):
        self.error = error
        return self

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.advance()
    def advance(self):
        self.token_idx +=1
        if self.token_idx < len(self.tokens):
            self.current_tok = self.tokens[self.token_idx]
        return self.current_tok
    def parse(self):
        result = self.expr()
        if not result.error and self.current_tok.type != TT_EOF:
            return result.failiure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end, "Expected Valid Operator:\n '*','+','/' or '-'"
            )) 
        return result
    def factor(self):
        res = ParseResult()
        token = self.current_tok
        if token.type in (TT_PLUS,TT_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(token,factor))
        if token.type in TT_LPAREN:
            res.register(self.advance())
            expr = res.register(self.expr)
            if res.error: return res
            if self.current_tok.type in TT_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failiure(InvalidSyntaxError(self.current_tok.pos_start,self.current_tok.pos_end, "Expected ')'"))

        elif token.type in (TT_INT,TT_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(token))
        return res.failiure(InvalidSyntaxError(token.pos_start,token.pos_end,"Expected Type Int or Float"))

    def term(self):
        return self.BinaryOp(self.factor,(TT_MUL, TT_DIV))
    def expr(self):
        return self.BinaryOp(self.term,(TT_PLUS, TT_MINUS))
    def BinaryOp(self,func,ops):
        res = ParseResult()
        left = res.register(func())
        if res.error: return res
        while self.current_tok.type in ops:
            op_token = self.current_tok
            res.register(self.advance())
            right = res.register(func())
            if res.error: return res
            left = BinaryOpNode(left,op_token,right)
        return res.success(left)

