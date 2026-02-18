
import ply.lex as lex
from language import tokens, reserved

t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'

t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_MULTIPLYEQUAL = r'\*='
t_DIVIDEQUAL = r'/='
t_MODEQUAL = r'%='
t_FLOOREQUAL = r'//='
t_POWEREQUAL = r'\^='

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_FLOOR = r'//'
t_POWER = r'\^'

t_OR = r'\|\|'
t_AND = r'\&\&'

t_INFEQ = r'<='
t_SUPEQ = r'>='

t_INF = r'<'
t_SUP = r'>'

t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_NOTEQ = r'!='

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_SEMI = r';'
t_COMA = r','

t_LBRACKET = r'\{'
t_RBRACKET = r'\}'

t_ignore = " \t"

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    s = t.value[1:-1]
    t.value = s.encode('utf-8').decode('unicode_escape')
    return t

def t_error(t):
    print("Illegal character", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
