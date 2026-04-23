names = [{}]
funct = {}


def tupleToList(node, keyword):
    if node == 'empty':
        return []
    if type(node) is not tuple or node[0] != keyword:
        return [node]

    elements = []
    for item in node[1:]:
        if item != 'empty':
            res = tupleToList(item, keyword)
            elements.extend(res)
    return elements


def findName(name):
    for scope in reversed(names):
        if name in scope:
            return scope[name]

    return None


def assign(name, value):
    scope = names[-1]
    scope[name] = value


def assign_existing(name, value):
    for scope in reversed(names):
        if name in scope:
            scope[name] = value
    assign(name, value)


def evalInst(start):
    stack = [start]

    while len(stack) != 0:
        p = stack.pop()

        if p == "empty":
            continue
        if type(p) is int:
            continue
        if type(p) is str:
            if p == "eval":
                from projet.parser import parser
                program = parser.parse(input())
                return evalInst(program[2])
            elif p == "scan":
                return evalInst(p)
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
                funct[p[1][0]] = (p[1][1], 'empty', False)
                if len(p) == 3:
                    stack.append(p[2])  # another define
                continue

            case 'function':
                if p[1] == 'empty': continue
                functionName = p[1][0]
                functionParam = p[1][1]
                functionBloc = p[1][2]

                isTerminal = False
                isReturn = functionBloc[2][0] == "return"
                if isReturn:
                    if len(functionBloc[2]) > 1 and type(functionBloc[2][1]) is tuple:
                        isCall = functionBloc[2][1][0] == "call"
                        if isCall:
                            sameName = functionBloc[2][1][1] == functionName
                            if sameName:
                                isTerminal = True
                                print(functionName, isTerminal)

                if functionName in funct:
                    if functionParam != funct[functionName][0]:
                        print("frérot corrige la taille")
                        return
                    bloc = funct[functionName][1]
                    if bloc is tuple:
                        print("Erreur : déja déclaré")
                        return
                    else:
                        funct[functionName] = (functionParam, functionBloc, isTerminal)
                else:
                    funct[functionName] = (functionParam, functionBloc, isTerminal)
                if len(p) == 3:
                    stack.append(p[2])
                continue

            case 'exit_scope':
                names.pop()
                continue

            case 'string':
                # it's not forgotten, it's normal
                continue

            case 'return':
                if len(p) > 1 and p[1] != 'empty':
                    return evalExpr(p[1])
                return None

            case 'for':
                stack.append(("for_call", p[2], p[4], p[3]))
                stack.append(p[1])  # i = 0
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

            case 'assign_op':
                return assign_op(p)

            case "assign":
                assign_existing(p[1], evalExpr(p[2]))
                continue

            case 'bloc':
                stack.append(p[2])
                stack.append(p[1])
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


def update(p):
    match p[2]:
        case '++':
            value = findName(p[1])
            if value is None:
                return None
            assign_existing(p[1], value + 1)
        case '--':
            value = findName(p[1])
            if value is None:
                return None
            assign_existing(p[1], value - 1)
    return findName(p[1])


def assign_op(p):
    if type(p) is int: return p
    if type(p) is str: return findName(p)

    operation = p[1]
    leftChild = p[2]
    rightChild = p[3]

    match operation:
        case '+=':
            value = findName(leftChild) + evalExpr(rightChild)
            assign_existing(leftChild, value)
        case '-=':
            value = findName(leftChild) - evalExpr(rightChild)
            assign_existing(leftChild, value)
        case '*=':
            value = findName(leftChild) * evalExpr(rightChild)
            assign_existing(leftChild, value)
        case '/=':
            value = findName(leftChild) / evalExpr(rightChild)
            assign_existing(leftChild, value)
        case '%=':
            value = findName(leftChild) % evalExpr(rightChild)
            assign_existing(leftChild, value)
        case '//=':
            value = findName(leftChild) // evalExpr(rightChild)
            assign_existing(leftChild, value)
        case '^=':
            value = findName(leftChild) ** evalExpr(rightChild)
            assign_existing(leftChild, value)
    return findName(leftChild)

def is_expr(p):
    if type(p) is int:
        return True
    if type(p) is str:
        return True
    if type(p) is tuple:
        op = p[0]
        valid_ops = {
            '+', '-', '*', '/', '==', '<', '>', '&&', '||', '<=', '>=', '%', '!=', '//', '^',
            'string', 'call', 'update'
        }
        if op in valid_ops:
            if len(p) == 3 and op not in ['string', 'update', 'call']:
                return is_expr(p[1]) and is_expr(p[2])
            return True
        return False
    return False

def checkExpression(p):
    if type(p) is tuple and len(p) >= 3 and p[0] == 'bloc':
        if p[1] != 'empty':
            return None
        expr = p[2]
    else:
        expr = p
    if is_expr(expr):
        return expr
    return None

def evalExpr(p):
    if type(p) is int: return p
    if type(p) is str and findName(p) is not None:
        return findName(p)
    if type(p) is str:
        if p == "scan":
            from projet.parser import parser

            inputValue = input()

            if inputValue[-1] == ';':
                print("ici c pas trancho")
                return None
            inputValue = inputValue + ';'
            program = parser.parse(inputValue)
            expr = checkExpression(program[2])
            if expr is not None:
                return evalExpr(expr)
            return None

        return p
    operation = p[0]
    leftChild = p[1]

    match operation:
        case 'update':
            return update(p)

        case 'string':
            return leftChild

        case 'call':
            functionName = leftChild
            args_node = p[2]
            if functionName not in funct:
                return None


            params_node = funct[functionName][0]
            list_args = tupleToList(args_node, 'args')
            list_params = tupleToList(params_node, 'params')

            if len(list_args) == len(list_params):
                evaluated_args = [evalExpr(arg) for arg in list_args]

                isTerminal = funct[functionName][2]

                names.append({})

                for i in range(len(list_params)):
                    assign(list_params[i], evaluated_args[i])

                ret_val = evalInst(funct[functionName][1])

                names.pop()
                return ret_val
            else:
                print("Problème côté arguments")
                return None

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
    if type(evalExpr(left)) is int and type(evalExpr(right)) is str:
        newRight = sum([ord(c) for c in evalExpr(right)])
    if type(evalExpr(left)) is str and type(evalExpr(right)) is int: newRight = str(evalExpr(right))
    return newRight
