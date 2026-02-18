names = {}

def evalInst(p):
    if p == 'empty': return
    if type(p) is int : return p
    if type(p) is str and p in names : return names[p]

    assert type(p) is tuple
    match p[0]:

        case 'for':
            evalInst(p[1])
            while evalExpr(p[2]) :
                evalInst(p[4])
                evalInst(p[3])
            return None

        case 'while':
            while evalExpr(p[1]): evalInst(p[2])
            return None

        case 'string':
            return p[1]

        case 'do_while':
            evalExpr(p[1])
            while evalExpr(p[2]): evalInst(p[1])
            return None

        case 'if':
            if evalExpr(p[1]): evalInst(p[2])
            elif len(p) == 4 and p[3][0] == 'else':
                evalInst(p[3][1])
            return None

        case "assign":
            if type(p[2]) is tuple: names[p[1]] = evalInst(p[2])
            else: names[p[1]] = evalExpr(p[2])
            return names[p[1]]

        case 'bloc':
            evalInst(p[1])
            evalInst(p[2])
            return None

        case 'update':
            return update(p)

        case 'assign_op':
            return assign_op(p)

        case 'print':
            res = evalInst(p[1])
            print('HitoCrok>', res)
            return res

        case 'multiple_print' :
            print('HitoCrok>', evalInst(p[1]), end=" ")
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
    if type(p) is str and p in names : return names[p]
    if type(p) is str : return p
    operation = p[0]
    leftChild = p[1]

    match operation:
        case 'string':
            return leftChild

    rightChild = ensureRightConcatType(leftChild, p[2])

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


def ensureRightConcatType(left, right):
    newRight = right
    if type(evalExpr(left)) is int and type(evalExpr(right)) is str: newRight = int(evalExpr(right))
    if type(evalExpr(left)) is str and type(evalExpr(right)) is int: newRight = str(evalExpr(right))
    return newRight