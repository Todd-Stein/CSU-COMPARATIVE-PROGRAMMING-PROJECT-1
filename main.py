import io
from queue import LifoQueue

treeStack = LifoQueue()

programSymbols = ["<let-in-end>", "{<let-in-end>}"]
letInEndSymbols = ["let", "<decl-list>", "in", "<type>", "(", "<expr>", ")" "end"]
declListSymbols = ["<decl>", "{<decl>}"]
declSymbols = ["id", ":", "<type>", "=", "<expr>", ";"]
typeSymbols = ["int", "real"]
exprSymbol = ["<term>", "+", "-", "<term>", "if", "<cond>", "then", "<expr>", "else", "<expr>"]
termSymbols= ["<factor>", "*", "/", "<factor>"]
factorSymbols = ["(", "<expr>", ")", "id", "number", "<type>", "(", "id", ")"]
conditionSymbols = ["<oprnd>", "<", "<=", ">", ">=", "==", "<>", "<oprnd>"]
operandSymbols = ["id", "num"]

def Oprnd(line: str):
    return True

def Cond(line: str):
    return True

def Factor(line: str):
    return True

def Term(line: str):
    return True

def Expr(line: str):
    return True

def Type(line: str):
    return True

def Decl(line: str):
    return True

def DeclList(line: [], idx: int):
     treeStack.put(2)
     symbolIndex = 0
     for index in range(idx, len(line)):
         if not line[index] =="":
             symbolIndex+=1

def LetInEnd(line: str):
    treeStack.put(1)
    symbolIndex = 0
    for index in range(0, len(line)):
        print()
        if not line[index] == "":
            if not line[index] == letInEndSymbols[symbolIndex]:
                match (letInEndSymbols[symbolIndex]):  
                    case "<decl-list>":
                        canContinue = DeclList(line, index)
                        if not canContinue:
                            return False
                        break
                    case "<type>":
                        canContinue = Type(line, index)
                        if not canContinue:
                            return False
                        break
                    case "<expr>":
                        canContinue = Type(line, index)
                        if not canContinue:
                            return False
            symbolIndex+=1     
    return True

def FindSymbols(line: str):
    splitLine = line.split("")
    #print(splitLine)
    #removeSpace = filter(splitLine, "")
    #print(removeSpace)
    #for lexeme in splitLine:
    validGrammar = False
    if treeStack.empty():
        treeStack.put(0)
        validGrammar = LetInEnd(line)
        if not validGrammar:
            print("Error in statement:" + str(line))
            exit()
        #if not lexeme == "":
        #    print(lexeme)

print("hello")
inFile = open("sample1.tiny")
for i in range(0, 5):
        line = inFile.readline()
        FindSymbols(line)