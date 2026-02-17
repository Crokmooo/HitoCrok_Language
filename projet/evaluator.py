names = {}

def evalInst(p):
    if p == 'empty': return
    if type(p) is int : return p
    if type(p) is str : return names[p]

    assert type(p) is tuple
    match p[0]:

        case 'for':
            evalInst(p[1])
            while evalExpr(p[2]) :
                evalInst(p[4])
                evalInst(p[3])

        case 'while':
            while evalExpr(p[1]): evalInst(p[2])

        case 'if':
            if evalExpr(p[1]): evalInst(p[2])
            elif len(p) == 4 and p[3][0] == 'else':
                evalInst(p[3][1])

        case "assign":
            names[p[1]] = evalExpr(p[2])
            return names[p[1]]

        case 'bloc':
            evalInst(p[1])
            evalInst(p[2])

        case 'update':
            return update(p)

        case 'assign_op':
            return assign_op(p)

        case 'print':
            res = evalInst(p[1])
            print('CALC>', res)
            return res

        case 'multiple_print' :
            print(evalInst(p[1]), end=" ")
            return evalInst(p[2])

        case 'other_print':
            if len(p) == 3:
                print(evalInst(p[1]), end=" ")
                return evalInst(p[2])
            else :
                print(evalInst(p[1]))
                return evalInst(p[1])

    return evalExpr(p)

def update(p):
    match p[2]:
        case '++':
            names[p[1]] += 1
        case '--':
            names[p[1]] -= 1
    return names[p[1]]

def assign_op(p):
    if type(p) is int: return p
    if type(p) is str: return names[p]

    operation = p[1]
    leftChild = p[2]
    rightChild = p[3]

    match operation:
        case '+=' : names[leftChild] += evalExpr(rightChild)
        case '-=' : names[leftChild] -= evalExpr(rightChild)
        case '*=' : names[leftChild] *= evalExpr(rightChild)
        case '/=' : names[leftChild] /= evalExpr(rightChild)
        case '%=' : names[leftChild] %= evalExpr(rightChild)
        case '//=' : names[leftChild] //= evalExpr(rightChild)
        case '^=' : names[leftChild] **= evalExpr(rightChild)
    return names[leftChild]


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
        case '<=' :
            return evalExpr(leftChild) <= evalExpr(rightChild)
        case '>=' :
            return evalExpr(leftChild) >= evalExpr(rightChild)
        case '%' :
            return evalExpr(leftChild) % evalExpr(rightChild)
        case '!=' :
            return evalExpr(leftChild) != evalExpr(rightChild)
        case '//' :
            return evalExpr(leftChild) // evalExpr(rightChild)
        case '^' :
            return evalExpr(leftChild) ** evalExpr(rightChild)
    return None
