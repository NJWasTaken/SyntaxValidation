import ply.lex as lex

tokens = [
    'IDENTIFIER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 
    'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE', 'EQUALS', 'NUMBER', 'COMMA', 
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'
]

# Reserved keywords
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN'
}

tokens = tokens + list(reserved.values())

# Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='

# Identifiers and reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Float Literal
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Number literal
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignoring whitespaces
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Newline handling
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()