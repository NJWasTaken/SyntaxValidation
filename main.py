from lexer import lexer
from parser import parser

print("------------------------------------------------------------------------")
print("Enter code line by line. Type 'end' on a new line to parse.")

input_data = ""

while True:
    line = input(">> ")
    if line.strip().lower() == "end":
        break
    input_data += line + "\n"

print("------------------------------------------------------------------------")

# Tokenize the input data
lexer.input(input_data)

# Parse the input data
print("\nParsing:")
parser.parse(input_data)
