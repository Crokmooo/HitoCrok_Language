from projet.evaluator import funct
from projet.parser import parser
from projet.lexer import lexer

f = open("terminal.txt")
s = f.read()
f.close()


parser.parse(s)
print(funct)
