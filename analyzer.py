from token import *
def tokenize(s, operators=[T_Addition, T_Substruction, T_Multi, T_Pow, T_Div], operand = T_Number):
    """
    generating basic trees:
        [ operator <- {left operand, right operand} ]
    TODO:
        add [0-9]+ operand groups
    """
    result = []
    n = len(s)
    i = 0
    
    keys = map(lambda e: e.pattern, operators)
    while i < n:
        if s[i] in keys:
            operator = operators[(keys.index(s[i]))]
            l = operand(i-1, s[i-1])
            r = operand(i+1, s[i+1])
            opr = operator()
            opr.l = l
            opr.r = r
            result.append(opr)
        i += 1
            
    return result


def analyze(o):
    """
    INPUT: array of operators
    making highest tree of sequently recieved operators
    """
    if len(o) < 2: return o[0]
    root = None
    i = 1
    while i < len(o):
        # swaping nodes with same r and l nodes
        if o[i - 1].w <= o[i].w:
            o[i - 1].r = o[i]
            o[i].root = o[i - 1]
            root = o[i - 1]

        if o[i - 1].w > o[i].w:
            # upper while ( o[i - 1].w > o[i].w )
            opl = o[i - 1]
            opr = o[i]
            while opl and opr.w <= opl.w:
                root = opl.root
                opl.root = opr
                opl.r = opr.l
                
                opr.root = root
                opr.l = opl
                
                opl = opr.root

        i += 1
    return root
            

def traverse(root):
    if isinstance(root, Operand):
        return root.val
    return root.action(traverse(root.l), traverse(root.r))