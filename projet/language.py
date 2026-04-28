reserved = {
    'print': 'PRINT',
    'trancho': 'EVAL',
    'sananes' : 'SCAN',
    'if' : "IF",
    'else' : 'ELSE',
    "for" : 'FOR',
    'while' : "WHILE",
    'do' : "DO",
    'funny' : 'FUNCTION',
    'return' : "RETURN"
}

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'INF', 'EQUALEQUAL', 'SUP', 'INFEQ', 'SUPEQ', 'NOTEQ'),
    ('left', 'PLUS', 'MINUS', 'PLUSPLUS', 'MINUSMINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO', 'POWER', 'FLOOR'),
    ('left', 'DOT', 'LCROCHET', 'RCROCHET')
)

tokens = ['INF', 'EQUALEQUAL', 'EQUAL', 'NAME', 'NUMBER', 'STRING', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'OR',
          'SUP', 'INFEQ', 'SUPEQ', 'MODULO', 'NOTEQ', 'PLUSPLUS', 'MINUSMINUS','PLUSEQUAL' ,'MINUSEQUAL' ,'MULTIPLYEQUAL' ,'DIVIDEQUAL' ,'MODEQUAL' ,'FLOOREQUAL' ,'POWEREQUAL',
          'AND', 'SEMI', 'COMA', 'LBRACKET', 'RBRACKET', 'POWER', 'FLOOR',
          'DOT', 'LCROCHET', 'RCROCHET'] + list(reserved.values())
