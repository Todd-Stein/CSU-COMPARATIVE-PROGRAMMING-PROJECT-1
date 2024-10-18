"""import io
from queue import LifoQueue

treeStack = LifoQueue()

programSymbols = ["<let-in-end>", "{<let-in-end>}"]
letInEndSymbols = ["let", "<decl-list>", "in", "<type>", "(", "<expr>", ")" "end"]
declListSymbols = ["<decl>"]
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
	canContinue = False
	#for index in range(idx, len(line)):
	index = idx
	canContinue = Decl(line, index)
	index += 1
	if not canContinue:
		return canContinue
	while not canContinue:
		canContinue = Decl(line, index)
		index += 1
	return True
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
	treeStack.pop()
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
"""
def IsLet():
	global lexeme
	return (lexeme[0]=="l" and lexeme[1]=="e" and lexeme[2]=="t")
def IgnoreSpace():
	global c
	while c == " ":
		GetChar()

def GetChar():
	#explicitly declaring scope because python sucks
	global c
	global file
	global fileIndex
	global cType
	global isALetter
	global isANumber
	global isUnknown
	c = file.read(1)
	fileIndex += 1
	file.seek(fileIndex)
	if c == None:
		print("Encountered EOF")
		exit()
	elif c.isalpha():
		cType = isALetter
		print(c + " is a letter")
	elif c.isnumeric():
		cType = isANumber
		print(c+" is a number")
	else:
		cType = isUnknown
		print(c+" is a special character")
def AssembleLexeme():
	global c
	global cType
	global isALetter
	global isANumber
	global lexeme
	global nextToken
	global LET
	global IDENT
	IgnoreSpace()
	if cType == isALetter:
		print(fileIndex)
		while cType == isALetter or cType == isANumber:
			lexeme.append(c)
			GetChar()
	if IsLet:
		nextToken = LET
		print("let statment")
	else:
		nextToken = IDENT
		print("identifier")
	print(lexeme)
def Let():
	global lexeme
	lexeme.clear()
	GetChar()
	AssembleLexeme()
def DeclList():
	return
def Decl():
	return
def Type():
	return
def Expr():
	return
def term():
	return
def Cond():
	return
def Oprnd():
	return
def ValidateAndRunStmnt():
	global c
	global nextToken
	global LET
	if nextToken == LET:
		Let()


import io
fileIndex = 0
file = None
lexeme = []
c = ""
#0 is alpha, 1 is num, 100 is unknown
cType = 0
nextToken = 0
isALetter = 0
isANumber = 1
isUnknown = 100

LET = 10
IDENT = 11
IN = 12
SEMICOLON = 13
END = 14
EQUAL = 15
GREATER = 16
LESS = 17
GREATEQUAL = 18
LESSEQUAL = 19
ASSIGN = 20
ADD = 21
SUB = 22
MULT = 23
DIV = 24
IF_STMNT = 25
THEN = 26
ELSE_STMNT = 27

file = open("sample1.tiny")
GetChar()
AssembleLexeme()
ValidateAndRunStmnt()
#while not c == None:
#	GetChar()
