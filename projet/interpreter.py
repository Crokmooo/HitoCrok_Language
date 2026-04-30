from projet.evaluator import funct, evalInst
from projet.graph import printTreeGraph
from projet.parser import parser
from projet.lexer import lexer
import projet.lexer as commentCount
f = open("terminal.txt")
s = f.read()
f.close()


program = parser.parse(s, lexer=lexer)
#printTreeGraph(program)
evalInst(program)
if (commentCount.numberOfComments > 0):
    print("HitoCrok - Admin> Tu as écrit", commentCount.numberOfComments, "commentaire", end="")
    if (commentCount.numberOfComments > 1):
        print("s", end="")
    print(". La honte.")
else :
    print("HitoCrok - Admin> Ok pas mal, 0 commentaire")