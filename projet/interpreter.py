from projet.parser import parser
from projet.lexer import lexer

s = '''
a = 0;
do {
    print(a);
    a = a + 1;
} while (a <= 10);
'''

parser.parse(s)
