DIGITS="0123456789" # Digit Constants
# Error Handling
class Error:
    def __init__(self,pos_start,pos_end,error_name,details):
        self.error_name = error_name
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.details = details
    def as_string(self):
        return f"File {self.pos_start.fn}, Line {self.pos_start.ln + 1}\n" + f'{self.error_name}:{self.details}'
class IllegalCharError(Error):
    def __init__(self,pos_start,pos_end,details):
        super().__init__(pos_start,pos_end,"Illegal Character",details)
# Positions
class Position:
    def __init__(self,index,line,column,fn,filetext):
        self.idx = index
        self.fn = fn
        self.ftxt = filetext
        self.ln = line
        self.col = column
    def advance(self, current_char):
        self.idx +=1
        self.col +=1
        if current_char == '\n':
            self.ln +=1
            self.col = 0
        return self
    def copy(self):
        return Position(self.idx,self.ln,self.col,self.fn,self.ftxt)
# Tokens for Lang
TT_INT		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'
class Token:
    def __init__(self,type_,value=None):
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
# Lexer for Lang
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
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start,self.pos,f"'{char}'")

        return tokens, None
        # Converts Integers and Floats into appendable tokens
    def make_numbers(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char ==".":
                if dot_count ==1: break
                dot_count+=1
                numstr+= "."
            else:
                    num_str += self.current_char
                    self.advance()
            if dot_count == 0:
                return Token(TT_INT, int(num_str))
            else:
                return Token(TT_FLOAT, float(num_str))
def run(fn,text):
    lexer = Lexer(fn,text)
    tokens, error = lexer.make_tokens()
    return tokens, error