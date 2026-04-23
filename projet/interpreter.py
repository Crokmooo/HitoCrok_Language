from projet.evaluator import funct, evalInst
from projet.graph import printTreeGraph
from projet.parser import parser
from projet.lexer import lexer

f = open("terminal.txt")
s = f.read()
f.close()


program = parser.parse(s, lexer=lexer)
print(program)
printTreeGraph(program)
evalInst(program)
print(funct)
