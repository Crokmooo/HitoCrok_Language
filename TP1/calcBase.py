# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:59:32 2024

@author: FB
"""
import uuid
import graphviz as gv

reserved = {
    'print': 'PRINT',
    'if' : "IF",
    'else' : 'ELSE',
    "for" : 'FOR',
    'while' : "WHILE",
}

# tokens = ( 'INF', 'EQUALEQUAL', 'EQUAL', 'NAME', 'NUMBER','MINUS', 'PLUS','TIMES','DIVIDE', 'LPAREN','RPAREN', 'OR', 'AND', 'SEMI' )
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_OR = r'\|'
t_AND = r'\&'
t_SEMI = r';'
t_INF = r'<'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
# t_NAME = r'[a-zA-Z_][a-zA-Z_0-9]*'
tokens = ['INF', 'EQUALEQUAL', 'EQUAL', 'NAME', 'NUMBER', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'OR',
          'AND', 'SEMI', 'LBRACKET', 'RBRACKET'] + list(reserved.values())


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')  # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'INF', 'EQUALEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

names = {}
import ply.lex as lex

lex.lex()


def evalInst(p):
    if p == 'empty': return
    assert type(p) is tuple
    if p[0] == 'bloc':
        evalInst(p[1])
        evalInst(p[2])
    if p[0] == 'print':
        print('CALC> ', evalExpr(p[1]))


def evalExpr(p):
    if type(p) is int: return p
    if p[0] == '+': return evalExpr(p[1]) + evalExpr(p[2])
    if p[0] == '*': return evalExpr(p[1]) * evalExpr(p[2])


def printTreeGraph(t):
    graph = gv.Digraph(format='pdf')
    graph.attr('node', shape='circle')
    addNode(graph, t)
    #graph.render(filename='img/graph') #Pour Sauvegarder
    graph.view() #Pour afficher

def addNode(graph, t):
    myId = uuid.uuid4()

    if type(t) != tuple:
        graph.node(str(myId), label=str(t))
        return myId

    graph.node(str(myId), label=str(t[0]))
    for i in range(1, len(t)):
         graph.edge(str(myId), str(addNode(graph, t[i])), arrowsize='0')


    return myId

def p_start(p):
    'start : bloc'
    print(p[1])
    printTreeGraph(p[1])
    evalInst(p[1])
    '''
    def p_expression_binop_plus(p): 
    'expression : expression PLUS expression' 
    #p[0] = p[1] + p[3] 
    p[0] = ('PLUS', p[1] , p[3]) 
    '''


def p_bloc(p):
    '''bloc : bloc statement SEMI
    | statement SEMI'''

    if len(p) == 4:
        p[0] = ('bloc', p[1], p[2])
    else:
        p[0] = ('bloc', 'empty', p[1])


def p_statement_assign(p):
    'statement : NAME EQUAL expression'
    names[p[1]] = p[3]


def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN'
    # print(p[3])
    p[0] = ('print', p[3])


def p_expression_binop_inf(p):
    'expression : expression INF expression'
    p[0] = p[1] < p[3]


def p_expression_binop_equal(p):
    'expression : expression EQUALEQUAL expression'
    p[0] = p[1] == p[3]


def p_expression_binop_and(p):
    'expression : expression AND expression'
    p[0] = p[1] and p[3]


def p_expression_binop_or(p):
    'expression : expression OR expression'
    p[0] = p[1] or p[3]


def p_expression_binop_plus(p):
    'expression : expression PLUS expression'
    # p[0] = p[1] + p[3]
    p[0] = ('+', p[1], p[3])


def p_expression_binop_times(p):
    'expression : expression TIMES expression'
    # p[0] = p[1] * p[3]
    p[0] = (p[2], p[1], p[3])


def p_expression_binop_divide_and_minus(p):
    '''expression : expression MINUS expression
     | expression DIVIDE expression'''
    if p[2] == '-':
        p[0] = p[1] - p[3]
    else:
        p[0] = p[1] / p[3]


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_expression_name(p):
    'expression : NAME'
    # p[0] = names[p[1]]
    p[0] = p[1]

def p_expression_if(p):
    'expression : IF LPAREN expression RPAREN LBRACKET bloc RBRACKET'
    if p[2] : p[0] = p[3]


def p_error(p):    print("Syntax error in input!")


import ply.yacc as yacc

yacc.yacc()
s = 'if(1<2){print(1+2);};'
yacc.parse(s)