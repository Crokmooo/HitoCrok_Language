names = {}
funct = {}


def evalInst(start):
    stack = [start]

    while len(stack) != 0:
        p = stack.pop()

        if p == "empty":
            continue
        if type(p) is int:
            continue
        if type(p) is str:
            continue

        assert type(p) is tuple

        declaration = p[0]

        match declaration:

            case 'program':
                stack.append(p[2])  # bloc
                stack.append(p[3])  # function
                stack.append(p[1])  # define
                continue

            case 'define':
                if p[1] == 'empty': continue
                funct[p[1][0]] = (p[1][1], 'empty')
                if len(p) == 3:
                    stack.append(p[2])  # another define
                continue

            case 'function':
                if p[1] == 'empty': continue
                functionName = p[1][0]
                functionParam = p[1][1]
                functionBloc = p[1][2]
                if functionName in funct:
                    bloc = funct[functionName][1]
                    if bloc is tuple:
                        print("Erreur : déja déclaré")
                    else:
                        funct[functionName] = (functionParam, functionBloc)
                else:
                    funct[functionName] = (functionParam, functionBloc)
                if len(p) == 3:
                    stack.append(p[2])
                continue

            case 'call':
                functionName = p[1]
                if p[1] in funct and len(p[2]) == len(funct[functionName][0]) and funct[functionName][1] != 'empty':
                    stack.append(funct[functionName][1])
                continue

            case 'string':
                # it's not forgotten, it's normal
                continue

            case 'for':
                stack.append(("for_call", p[2], p[4], p[3]))
                stack.append(p[1]) # i = 0
                continue

            case 'for_call':
                forCondition = p[1]
                forBloc = p[2]
                forUpdate = p[3]

                if evalExpr(forCondition):
                    stack.append(("for_call", forCondition, forBloc, forUpdate))
                    stack.append(forUpdate)
                    stack.append(forBloc)
                continue

            case 'while':
                if evalExpr(p[1]):
                    stack.append(p)
                    stack.append(('while_call', p[2]))
                continue

            case 'while_call':
                bloc = p[1]
                stack.append(bloc)
                continue

            case 'do_while':
                stack.append(("while", p[2], p[1]))
                stack.append(p[1])
                continue

            case 'if':
                if evalExpr(p[1]):
                    stack.append(p[2])
                elif len(p) == 4 and p[3][0] == 'else':
                    stack.append(p[3][1])
                continue

            case "assign":
                names[p[1]] = evalExpr(p[2])
                continue

            case 'bloc':
                stack.append(p[2])
                stack.append(p[1])
                continue

            case 'update':
                update(p)
                continue

            case 'assign_op':
                assign_op(p)
                continue

            case 'print':
                res = evalExpr(p[1])
                print('HitoCrok>', res)
                continue

            case 'multiple_print':
                print('HitoCrok>', evalExpr(p[1]), end=" ")
                stack.append(p[2])
                continue

            case 'other_print':
                if len(p) == 3:
                    print(evalExpr(p[1]), end=" ")
                    stack.append(p[2])
                else:
                    print(evalExpr(p[1]))
                continue

            case _:
                evalExpr(p)

        print(12)


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
        case '+=':
            names[leftChild] += evalExpr(rightChild)
        case '-=':
            names[leftChild] -= evalExpr(rightChild)
        case '*=':
            names[leftChild] *= evalExpr(rightChild)
        case '/=':
            names[leftChild] /= evalExpr(rightChild)
        case '%=':
            names[leftChild] %= evalExpr(rightChild)
        case '//=':
            names[leftChild] //= evalExpr(rightChild)
        case '^=':
            names[leftChild] **= evalExpr(rightChild)
    return names[leftChild]


def evalExpr(p):
    if type(p) is int: return p
    if type(p) is str and p in names: return names[p]
    if type(p) is str: return p
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
        case '<':
            return evalExpr(leftChild) < evalExpr(rightChild)
        case '>':
            return evalExpr(leftChild) > evalExpr(rightChild)
        case '&&':
            return evalExpr(leftChild) and evalExpr(rightChild)
        case '||':
            return evalExpr(leftChild) or evalExpr(rightChild)
        case '<=':
            return evalExpr(leftChild) <= evalExpr(rightChild)
        case '>=':
            return evalExpr(leftChild) >= evalExpr(rightChild)
        case '%':
            return evalExpr(leftChild) % evalExpr(rightChild)
        case '!=':
            return evalExpr(leftChild) != evalExpr(rightChild)
        case '//':
            return evalExpr(leftChild) // evalExpr(rightChild)
        case '^':
            return evalExpr(leftChild) ** evalExpr(rightChild)
    return None


def ensureRightConcatType(left, right):
    newRight = right
    if type(evalExpr(left)) is int and type(evalExpr(right)) is str: newRight = int(evalExpr(right))
    if type(evalExpr(left)) is str and type(evalExpr(right)) is int: newRight = str(evalExpr(right))
    return newRight
