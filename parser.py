import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''program : function_list'''
    print("Successfully parsed.")

def p_function_list(p):
    '''function_list : function_definition
                    | function_list function_definition'''

def p_function_definition(p):
    '''function_definition : INT IDENTIFIER LPAREN array_param_list RPAREN compound_statement
                         | FLOAT IDENTIFIER LPAREN array_param_list RPAREN compound_statement'''
    print(f"Parsed function '{p[2]}' with return type '{p[1]}'")


def p_compound_statement(p):
    '''compound_statement : LBRACE statement_list RBRACE'''

def p_array_param_list(p):
    '''array_param_list : array_param
                       | param
                       | array_param_list COMMA array_param
                       | array_param_list COMMA param
                       | empty'''

def p_array_param(p):
    '''array_param : INT IDENTIFIER LBRACKET NUMBER RBRACKET
                  | FLOAT IDENTIFIER LBRACKET NUMBER RBRACKET'''
    print(f"Parsed array parameter: {p[2]}[{p[4]}]")

def p_param(p):
    '''param : INT IDENTIFIER
            | FLOAT IDENTIFIER'''
  

def p_statement_list(p):
    '''statement_list : statement
                     | statement_list statement
                     | empty'''
    pass

def p_statement(p):
    '''statement : declaration
                | assignment
                | selection_statement
                | return_statement
                | compound_statement'''
    pass

def p_declaration(p):
    '''declaration : INT var_list SEMICOLON
                  | FLOAT var_list SEMICOLON
                  | INT IDENTIFIER EQUALS expression SEMICOLON
                  | FLOAT IDENTIFIER EQUALS expression SEMICOLON'''


def p_var_list(p):
    '''var_list : variable
                | var_list COMMA variable'''
    pass

def p_variable(p):
    '''variable : IDENTIFIER
                | IDENTIFIER LBRACKET NUMBER RBRACKET'''
    pass

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression SEMICOLON
                 | IDENTIFIER LBRACKET NUMBER RBRACKET EQUALS expression SEMICOLON'''

def p_selection_statement(p):
    '''selection_statement : IF LPAREN expression RPAREN statement
                         | IF LPAREN expression RPAREN statement ELSE statement'''
    print("Parsed selection statement")

def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON'''

def p_expression(p):
    '''expression : term
                 | expression PLUS term
                 | expression MINUS term'''
    pass

def p_term(p):
    '''term : factor
            | term MULTIPLY factor
            | term DIVIDE factor'''
    pass

def p_factor(p):
    '''factor : NUMBER
              | FLOAT
              | array_access
              | IDENTIFIER
              | LPAREN expression RPAREN'''
    pass

def p_array_access(p):
    '''array_access : IDENTIFIER LBRACKET NUMBER RBRACKET
                   | IDENTIFIER LBRACKET IDENTIFIER RBRACKET'''
    pass

def p_comparison(p):
    '''expression : expression GT expression
                 | expression LT expression
                 | expression GE expression
                 | expression LE expression
                 | expression EQ expression
                 | expression NE expression'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type: {p.type}) on line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# int sum(int arr[10]) {
#     int total = 0;
#     if (total < 100) {
#         return total;
#     }
#     return total + arr[0];
# }

# float average(float values[5]) {
#     float total = 0.0;
#     values[0] = 1.5;
#     return total;
# }

# int max(int a, int b) {
#     if (a > b) {
#         return a;
#     } else {
#         return b;
#     }
# }
# end