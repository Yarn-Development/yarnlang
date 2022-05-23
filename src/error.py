from sarrows import string_with_arrows
# Error Handling
class Error:
    def __init__(self,pos_start,pos_end,error_name,details):
        self.error_name = error_name
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.details = details
    def as_string(self):
        return f"File {self.pos_start.fn}, Line {self.pos_start.ln + 1}\n" + f'{self.error_name}:{self.details}' + f"\n\n{string_with_arrows(self.pos_start.ftxt,self.pos_start,self.pos_end)}"
class IllegalCharError(Error):
    def __init__(self,pos_start,pos_end,details=''):
        super().__init__(pos_start,pos_end,"Illegal Character",details)
class InvalidSyntaxError(Error):
    def __init__(self,pos_start,pos_end,details=''):
        super().__init__(pos_start,pos_end,"Invalid Syntax",details)