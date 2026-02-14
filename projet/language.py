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
    ('nonassoc', 'INF', 'EQUALEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

tokens = ['INF', 'EQUALEQUAL', 'EQUAL', 'NAME', 'NUMBER', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'OR', 'SUP',
          'AND', 'SEMI', 'LBRACKET', 'RBRACKET'] + list(reserved.values())