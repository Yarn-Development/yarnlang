from tokens import *
from position import Position
from error import IllegalCharError
class Lexer:
    def __init__(self,fn,text):
        self.fn = fn # Name of File being Lexed
        self.text = text # Text to be lexed
        self.pos = Position(-1,0,-1,self.fn,text) # Position of character in Lexer
        self.current_char = None # Current Character being Lexed
        self.advance() # Increments next char
    def advance(self):
        self.pos.advance(self.current_char) # Advances to next char
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None # Verifies there is more characters, if none process ends
    # Creates Tokens for each operator
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t': # Skips Tabs and Spaces
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_numbers())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS,pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS,pos_start=self.pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL,pos_start=self.pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV,pos_start=self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN,pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN,pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start,self.pos,f"'{char}'")
        tokens.append(Token(TT_EOF,pos_start=self.pos))
        return tokens, None
        # Converts Integers and Floats into appendable tokens
    def make_numbers(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()
        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char ==".":
                if dot_count ==1: break
                dot_count+=1
                numstr+= "."
            else:
                    num_str += self.current_char
                    self.advance()
            if dot_count == 0:
                return Token(TT_INT, int(num_str),pos_start,self.pos)
            else:
                return Token(TT_FLOAT, float(num_str),pos_start,self.pos)