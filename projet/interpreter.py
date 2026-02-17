from projet.parser import parser
from projet.lexer import lexer

s = '''
x = 10;
x += 1;
for (x=1; x < 5; x++){
    print(1+1,x,6,7,8,9,10);
};

'''

parser.parse(s)
