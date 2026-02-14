from projet.parser import parser
from projet.lexer import lexer

s = ('for (x=5;x>1;x=x-1) { print(x); };'
     'for (x=1;x<100;x=x+2) { print(x); };print(5/2);')

parser.parse(s)