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


def p_statement_assign(p):
    """statement : NAME EQUAL expression"""
    p[0] = ("assign", p[1], p[3])


def p_statement_print(p):
    """statement : PRINT LPAREN expression RPAREN"""
    p[0] = ("print", p[3])


def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression INF expression
                  | expression SUP expression
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

def p_expression_name(p):
    """expression : NAME"""
    p[0] = p[1]

def p_statement_if(p):
    """statement : IF LPAREN expression RPAREN LBRACKET bloc RBRACKET"""
    p[0] = ('if', p[3], p[6])

def p_statement_else(p):
    """statement : IF LPAREN expression RPAREN LBRACKET bloc RBRACKET ELSE LBRACKET bloc RBRACKET"""
    p[0] = ('if', p[3], p[6], ('else', p[10]))

def p_statement_for(p):
    """statement : FOR LPAREN statement SEMI expression SEMI statement RPAREN LBRACKET bloc RBRACKET"""
    p[0] = ('for', p[3], p[5], p[7], p[10])


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()
