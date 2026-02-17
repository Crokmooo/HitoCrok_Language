reserved = {
    'print': 'PRINT',
    'if' : "IF",
    'else' : 'ELSE',
    "for" : 'FOR',
    'while' : "WHILE",
}

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'INF', 'EQUALEQUAL', 'SUP', 'INFEQ', 'SUPEQ', 'NOTEQ'),
    ('left', 'PLUS', 'MINUS', 'PLUSPLUS', 'MINUSMINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO', 'POWER', 'FLOOR')
)

tokens = ['INF', 'EQUALEQUAL', 'EQUAL', 'NAME', 'NUMBER', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'OR',
          'SUP', 'INFEQ', 'SUPEQ', 'MODULO', 'NOTEQ', 'PLUSPLUS', 'MINUSMINUS','PLUSEQUAL' ,'MINUSEQUAL' ,'MULTIPLYEQUAL' ,'DIVIDEQUAL' ,'MODEQUAL' ,'FLOOREQUAL' ,'POWEREQUAL',
          'AND', 'SEMI', 'LBRACKET', 'RBRACKET', 'POWER', 'FLOOR'] + list(reserved.values())
