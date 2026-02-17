from projet.parser import parser
from projet.lexer import lexer

s = '''
x = 10;
x += 1;
print(x++);
'''

parser.parse(s)
