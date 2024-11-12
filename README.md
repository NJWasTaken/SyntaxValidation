# Syntax Validation

Welcome to **SyntaxValidation**! This project includes a lexer, parser, and main driver to validate syntax for a custom language. This repository demonstrates the fundamentals of lexical analysis and syntax parsing, offering a streamlined way to validate code syntax.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project breaks down the syntax validation process into distinct stages:
1. **Lexical Analysis**: Using `lexer.py`, the project tokenizes input, converting code into meaningful tokens.
2. **Parsing**: `parser.py` analyzes the tokenized input, ensuring the code conforms to the expected syntax.
3. **Execution**: `main.py` ties everything together, running the lexer and parser to validate the syntax of given code snippets.

## Features

- **Tokenization**: Recognizes keywords, operators, identifiers, and literals.
- **Syntax Parsing**: Verifies correct structure and order of tokens.
- **Error Detection**: Identifies common syntax errors.
  
## Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NJWasTaken/SyntaxValidation.git
   cd SyntaxValidation
   ```

2. Install any required dependencies:
   ```bash
   pip install ply==3.11
   ```
   
## Project Structure

- **lexer.py** - Handles tokenization of the input code.
- **parser.py** - Parses tokens and checks for syntax validity.
- **main.py** - Main script to run the lexer and parser on input files.

## Contributing

Contributions are welcome! Feel free to fork this repository, make your improvements, and submit a pull request.
