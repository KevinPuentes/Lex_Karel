#https://www.dabeaz.com/ply/PLYTalk.pdf

import ply.lex as lex

tokens = ['NAME', 'NUMBER', 'EQUALS', 'JUMPLINE','LPAREN','RPAREN']
reserved = {'AVANZA' : 'FRONT', 'GIRA-IZQUIERDA':'LEFT', 'COGE-ZUMBADOR':'TAKE', 'DEJA-ZUMBADOR':'LET'}
tokens += reserved.values()

t_ignore = ' \t'
t_FRONT = r'AVANZA'
t_LEFT = r'GIRA-IZQUIERDA'
t_TAKE = r'COGE-ZUMBADOR'
t_LET = r'DEJA-ZUMBADOR'
t_EQUALS = r'='
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_JUMPLINE = r'\n'
#t_NAME = r'[a-zA-Z_]'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore_WHITESPACES = r"[ \t]+"

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

# Error handling rule
def t_error(token):
    message = "Token desconocido:"
    message = "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    #raise Exception(message)

lex.lex() # Build the lexer

entrada = open("Expresions.in","r")
exp = entrada.readlines()

for i in range(0, len(exp)):    
    pp = exp[i]
    str1 = str(pp)
    print ("------####-------")
    print (str1)
    #print ("P")
    lex.input(str1)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
