from projet.parser import parser
from projet.lexer import lexer

s = '''
a = 5;
while (a) {
    print(a);
    a--;
};
'''

parser.parse(s)
