names = {}

def evalInst(p):
    if p == 'empty': return
    assert type(p) is tuple
    match p[0]:

        case 'for':
            evalInst(p[1])
            while evalExpr(p[2]) :
                evalInst(p[4])
                evalInst(p[3])

        case 'if':
            if evalExpr(p[1]): evalInst(p[2])
            elif len(p) == 4 and p[3][0] == 'else':
                evalInst(p[3][1])

        case "assign":
            names[p[1]] = evalExpr(p[2])

        case 'bloc':
            evalInst(p[1])
            evalInst(p[2])

        case 'print':
            print('CALC> ', evalExpr(p[1]))


def evalExpr(p):
    if type(p) is int : return p
    if type(p) is str : return names[p]

    operation = p[0]
    leftChild = p[1]
    rightChild = p[2]

    match operation:
        case '*':
            return evalExpr(leftChild) * evalExpr(rightChild)
        case '+':
            return evalExpr(leftChild) + evalExpr(rightChild)
        case '-':
            return evalExpr(leftChild) - evalExpr(rightChild)
        case '/':
            return evalExpr(leftChild) / evalExpr(rightChild)
        case '==':
            return evalExpr(leftChild) == evalExpr(rightChild)
        case '<' :
            return evalExpr(leftChild) < evalExpr(rightChild)
        case '>' :
            return evalExpr(leftChild) > evalExpr(rightChild)
        case '&&' :
            return evalExpr(leftChild) and evalExpr(rightChild)
        case '||' :
            return evalExpr(leftChild) or evalExpr(rightChild)
    return None
