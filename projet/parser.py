import ply.yacc as yacc

from projet.evaluator import evalInst
from projet.graph import printTreeGraph
from projet.language import tokens, precedence

def p_start(p):
    """start : bloc"""
    print(p[1])
    printTreeGraph(p[1])
    evalInst(p[1])

def p_bloc(p):
    """bloc : bloc statement SEMI
            | statement SEMI"""

    if len(p) == 4:
        p[0] = ('bloc', p[1], p[2])
    else:
        p[0] = ('bloc', 'empty', p[1])

def p_printable(p):
    """printable : expression
                 | assignement
                 | update"""
    p[0] = p[1]

def p_statement_simple(p):
    """statement : printable"""
    p[0] = p[1]

def p_statement_assign(p):
    """statement : NAME EQUAL expression"""
    p[0] = ("assign", p[1], p[3])


def p_statement_print(p):
    """statement : PRINT LPAREN printable RPAREN"""
    p[0] = ("print", p[3])

def p_statement_print_multiple(p):
    """statement : PRINT LPAREN printable COMA other_print RPAREN"""
    p[0] = ("multiple_print", p[3], p[5])

def p_statement_print_otherprint(p):
    """other_print : printable COMA other_print
                | printable"""
    if len(p) == 4 :
        p[0] = ("other_print", p[1], p[3])
    else :
        p[0] = ("other_print", p[1])

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression INFEQ expression
                  | expression SUPEQ expression
                  | expression NOTEQ expression
                  | expression INF expression
                  | expression SUP expression
                  | expression FLOOR expression
                  | expression POWER expression
                  | expression EQUALEQUAL expression
                  | expression AND expression
                  | expression OR expression"""

    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_assignment_operation(p):
    """assignement : expression PLUSEQUAL expression
                 | expression MINUSEQUAL expression
                 | expression MULTIPLYEQUAL expression
                 | expression DIVIDEQUAL expression
                 | expression MODEQUAL expression
                 | expression FLOOREQUAL expression
                 | expression POWEREQUAL expression"""

    p[0] = ('assign_op', p[2], p[1], p[3])

def p_expression_name(p):
    """expression : NAME"""
    p[0] = p[1]

def p_statement_update(p):
    """update : NAME PLUSPLUS
              | NAME MINUSMINUS"""
    p[0] = ('update', p[1], p[2])

def p_expression_string(p):
    """expression : STRING"""
    p[0] = ('string', p[1])

def p_statement_if(p):
    """statement : IF LPAREN expression RPAREN LBRACKET bloc RBRACKET"""
    p[0] = ('if', p[3], p[6])

def p_statement_else(p):
    """statement : IF LPAREN expression RPAREN LBRACKET bloc RBRACKET ELSE LBRACKET bloc RBRACKET"""
    p[0] = ('if', p[3], p[6], ('else', p[10]))

def p_statement_for(p):
    """statement : FOR LPAREN statement SEMI expression SEMI statement RPAREN LBRACKET bloc RBRACKET"""
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_statement_while(p):
    """statement : WHILE LPAREN expression RPAREN LBRACKET bloc RBRACKET"""
    p[0] = ('while', p[3], p[6])

def p_statement_do_while(p):
    """statement : DO LBRACKET bloc RBRACKET WHILE LPAREN expression RPAREN"""
    p[0] = ('do_while', p[3], p[7])

def p_error(p):
    print("Syntax error")


parser = yacc.yacc()
