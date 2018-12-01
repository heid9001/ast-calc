# T
class Operator(object):
    w = None
    pattern = None
    root = None
    
    def __int__(self):
        self.r = None
        self.l = None
        self.root = None
        
    def action(self, a, b):
        pass
        
    def traverse(self):
        
        if isinstance(self.l, Operator):
            self.l.traverse()
        if isinstance(self.r, Operator):
            self.r.traverse()
            
        print self, self.l, self.r
            
    def __len__(self):
        r = 1 + len(self.r)
        l = 1 + len(self.l)
        return max([r, l])
        
    def __repr__(self):
        return "%s"%(self.pattern)


class Operand(object):
    pattern = None
    py_type = None
    
    def __init__(self, pos, val):
        self.pos = pos
        self.val = self.py_type(val)
        
    def __eq__(self, o):
        return o.pos == self.pos
    
    def __hash__(self):
        return o.pos
        
    def __len__(self):
        return 1
        
    def __repr__(self):
        return "%s"%(self.val)
        
        

# Ariphmetic operators
class T_Addition(Operator):
    w = 1
    pattern = "+"
    
    def action(self, a, b):
        return a + b
        

class T_Substruction(Operator):
    w = 1
    pattern = "-"
    
    def action(self, a, b):
        return a - b


class T_Multi(Operator):
    w = 2
    pattern = "*"
    
    def action(self, a, b):
        return a * b


class T_Div(Operator):
    w = 2
    pattern = "/"
    
    def action(self, a, b):
        return a // b
        
class T_Pow(Operator):
    w = 3
    pattern = "^"
    
    def action(self, a, b):
        return a ** b
    

# Operands (Liefs)
class T_Number(Operand):
    pattern = "([0-9]+)"
    py_type = int