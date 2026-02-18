reserved = {
    'print': 'PRINT',
    'if' : "IF",
    'else' : 'ELSE',
    "for" : 'FOR',
    'while' : "WHILE",
    'do' : "DO",
}

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'INF', 'EQUALEQUAL', 'SUP', 'INFEQ', 'SUPEQ', 'NOTEQ'),
    ('left', 'PLUS', 'MINUS', 'PLUSPLUS', 'MINUSMINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO', 'POWER', 'FLOOR')
)

tokens = ['INF', 'EQUALEQUAL', 'EQUAL', 'NAME', 'NUMBER', 'STRING', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'OR',
          'SUP', 'INFEQ', 'SUPEQ', 'MODULO', 'NOTEQ', 'PLUSPLUS', 'MINUSMINUS','PLUSEQUAL' ,'MINUSEQUAL' ,'MULTIPLYEQUAL' ,'DIVIDEQUAL' ,'MODEQUAL' ,'FLOOREQUAL' ,'POWEREQUAL',
          'AND', 'SEMI', 'COMA', 'LBRACKET', 'RBRACKET', 'POWER', 'FLOOR'] + list(reserved.values())
