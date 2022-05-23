class NumberNode:
    def __init__(self,tok):
        self.tok = tok
    def __repr__(self):
        return f"{self.tok}"
class BinaryOpNode:
    def __init__(self,left_node,op_token,right_node):
        self.left_node = left_node
        self.right_node = right_node
        self.op_token = op_token
    def __repr__(self):
        return f"({self.left_node}, {self.op_token}, {self.right_node})"
class UnaryOpNode:
    def __init__(self,op_token,node):
        self.op_token = op_token
        self.node = node
    def __repr__(self):
        return f"{self.op_token}, {self.node}"