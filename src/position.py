class Position:
    def __init__(self,index,line,column,fn,filetext):
        self.idx = index
        self.fn = fn
        self.ftxt = filetext
        self.ln = line
        self.col = column
    def advance(self, current_char=None):
        self.idx +=1
        self.col +=1
        if current_char == '\n':
            self.ln +=1
            self.col = 0
        return self
    def copy(self):
        return Position(self.idx,self.ln,self.col,self.fn,self.ftxt)