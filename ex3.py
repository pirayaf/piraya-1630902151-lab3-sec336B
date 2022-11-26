OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}

def postfix(expr):
    opr_s = []
    out_s = ""
    for ch in expr:
        if ch not in OPERATORS:
            out_s+=ch
        elif ch =='(':  
            opr_s.append('(')
        elif ch ==')':
            while opr_s and opr_s[-1]!= '(':
                out_s+=opr_s.pop()
            opr_s.pop()
        else:
            while opr_s and opr_s[-1]!='(' and PRIORITY[ch]<=PRIORITY[opr_s[-1]]:
                out_s+=opr_s.pop()
            opr_s.append(ch)
    while opr_s:
        out_s+=opr_s.pop()
    return out_s

expr = "A + B"
print("Initial value: ",expr)
print("Result value: ",postfix(expr))
print("\n")

expr = "A - B"
print("Initial value: ",expr)
print("Result value: ",postfix(expr))
print("\n")

expr = "A + B - C"
print("Initial value: ",expr)
print("Result value: ",postfix(expr))
print("\n")

expr = "A * B"
print("Initial value: ",expr)
print("Result value: ",postfix(expr))
print("\n")

expr = "( A + B ) * C"
print("Initial value: ",expr)
print("Result value: ",postfix(expr))
print("\n")

expr = "A * ( B + C )"
print("Initial value: ",expr)
print("Result value: ",postfix(expr))
print("\n")

