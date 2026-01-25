from enum import Enum, auto

Token = Enum("Token", [
        # Parentheses
        "LPAREN",       # (
        "RPAREN",       # )
        "LBRACE",       # {
        "RBRACE",       # {
        "LSQUARE",      # [
        "RSQUARE",      # ]
        "ARRAY",        # []

        # Mutation operators
        "ASSIGN",       # =
        "INC",          # ++
        "DEC",          # --
        "ADDASSIGN",    # +=
        "MULASSIGN",    # *=
        "SUBASSIGN",    # -=
        "DIVASSIGN",    # /=
        "LANDASSIGN",   # &=
        "LORASSIGN",    # |=
        "MODASSIGN",    # %=

        # Unary operators
        "NOT",          # !

        # Binary operators
        "ADD",          # +
        "MUL",          # *
        "SUB",          # -
        "ARROW",        # ->
        "DIV",          # /
        "MOD",          # %
        "LT",           # <
        "LE",           # <=
        "LSHIFT",       # <<
        "GT",           # >
        "GE",           # >=
        "RSHIFT",       # >>
        "EQ",           # ==
        "NE",           # !=
        "LAND",         # &
        "LOR",          # |
        "AND",          # &&
        "OR",           # ||

        # Ternary operators
        "QUERY",        # ?
        "COLON",        # :

        # Punctuation
        "DOT",          # .
        "COMMA",        # ,
        "SEMICOLON",    # ;

        # Keywords
        "IF",           # if
        "FOR",          # for
        "WHILE",        # while
        "RETURN",       # return
        "SIZEOF",       # sizeof
        "STATIC",       # static
        "CONST",        # const
        "TYPEDEF",      # typedef
        "STRUCT",       # struct

        # Types
        "VOID_T",       # void
        "CHAR_T",       # char
        "SHORT_T",      # short
        "INT_T",        # int
        "LONG_T",       # long
        "FLOAT_T",      # float
        "DOUBLE_T",     # double
        "SIGNED_T",     # signed
        "UNSIGNED_T",   # unsigned
        "BOOL_T",       # bool

        # Notable functions
        "MALLOC",       # malloc
        "CALLOC",       # calloc
        "FREE",         # free
        "STRLEN",       # strlen
        "STRCMP",       # strcmp
        "PRINTF",       # printf
        "FPRINTF",      # fprintf

        # Literals
        "NUMBER",       # 123
        "STRING",       # "abc"
        "CHAR",         # 'a'
        "NULL",         # NULL
        "STDIN",        # stdin
        "STDOUT",       # stdout
        "STDERR",       # stderr

        "IDENTIFIER",   # abc
        "UNEXPECTED",   # ???
        "EOF",          # EOF
    ],
    start = 0
)

keywords: dict[str, Token] = {
    # Keywords
    "if":       Token.IF,
    "for":      Token.FOR,
    "while":    Token.WHILE,
    "return":   Token.RETURN,
    "sizeof":   Token.SIZEOF,
    "static":   Token.STATIC,
    "const":    Token.CONST,
    "typedef":  Token.TYPEDEF,
    "struct":   Token.STRUCT,

    # Types
    "void":     Token.VOID_T,
    "char":     Token.CHAR_T,
    "short":    Token.SHORT_T,
    "int":      Token.INT_T,
    "long":     Token.LONG_T,
    "float":    Token.FLOAT_T,
    "double":   Token.DOUBLE_T,
    "signed":   Token.SIGNED_T,
    "unsigned": Token.UNSIGNED_T,
    "bool":     Token.BOOL_T,

    # Notable functions
    "malloc":   Token.MALLOC,
    "calloc":   Token.CALLOC,
    "free":     Token.FREE,
    "strcmp":   Token.STRCMP,
    "strlen":   Token.STRLEN,
    "printf":   Token.PRINTF,
    "fprintf":  Token.FPRINTF,

    # Literals
    "NULL":     Token.NULL,
    "stdin":    Token.STDIN,
    "stdout":   Token.STDOUT,
    "stderr":   Token.STDERR,
}

def is_number(c: str) -> bool:
    return ord(c) >= ord("0") and ord(c) <= ord("9")

def is_alpha(c: str) -> bool:
    c1 = c == "_"
    c2 = ord(c) >= ord("a") and ord(c) <= ord("z")
    c3 = ord(c) >= ord("A") and ord(c) <= ord("Z")
    return c1 or c2 or c3

def is_alphanumeric(c: str) -> bool:
    return is_alpha(c) or is_number(c)

def is_whitespace(c: str) -> bool:
    return c in [" ", "\t", "\n"]

def is_type(token: Token) -> bool:
    return token.value >= Token.CHAR_T.value and token.value <= Token.VOID_T.value

class Lexer:
    def __init__(self, s: str):
        self.s = s
        self.i = 0
        self.cache = None

    def consume_comment(self):
        while self.s[self.i] != "\n":
            self.i += 1

    def consume_line(self) -> str:
        s = ""
        while self.s[self.i] != "\n":
            s += self.s[self.i]
            self.i += 1
        return s

    def consume_whitespace(self):
        while is_whitespace(self.__peek()):
            self.i += 1

    def consume_number(self):
        while True:
            c = self.__peek()
            if c == "" or not is_number(c): break
            self.i += 1

        if self.__peek() == "e":
            self.i += 1
            while True:
                c = self.__peek()
                if c == "" or not is_number(c): break
                self.i += 1

        self.i -= 1

    def consume_alphanumeric(self) -> str:
        s = ""
        while is_alphanumeric(self.__peek()):
            s += self.s[self.i]
            self.i += 1
        self.i -= 1
        return s

    def consume_string(self):
        self.i += 1
        while self.i < len(self.s) and self.s[self.i] != "\"":
            if self.s[self.i] == "\\": self.i += 1
            self.i += 1

    def consume_char(self):
        self.i += 1
        if self.i < len(self.s):
            if self.s[self.i] == "\\": self.i += 2
            else: self.i += 1

    def __peek(self) -> str:
        return self.s[self.i] if self.i < len(self.s) else ""

    def __peek_next(self) -> str:
        return self.s[self.i+1] if self.i+1 < len(self.s) else ""

    def peek(self) -> Token:
        if self.cache == None:
            self.cache = self.consume()
        return self.cache

    def consume(self) -> Token:
        token = Token.UNEXPECTED

        if self.cache:
            token = self.cache
            self.cache = None

        while token == Token.UNEXPECTED:
            self.consume_whitespace()

            match self.__peek():
                case "(": token = Token.LPAREN
                case ")": token = Token.RPAREN
                case "{": token = Token.LBRACE
                case "}": token = Token.RBRACE
                case "[":
                    if self.__peek_next() == "]":
                        self.i += 1
                        token = Token.ARRAY
                    else:
                        token = Token.LSQUARE
                case "]": token = Token.RSQUARE
                case ".": token = Token.DOT
                case ",": token = Token.COMMA
                case ";": token = Token.SEMICOLON

                case "+":
                    match self.__peek_next():
                        case "+":
                            self.i += 1
                            token = Token.INC
                        case "=":
                            self.i += 1
                            token = Token.ADDASSIGN
                        case _:
                            token = Token.ADD

                case "*":
                    if self.__peek_next() == "=":
                        self.i += 1
                        token = Token.MULASSIGN
                    else:
                        token = Token.MUL

                case "-":
                    match self.__peek_next():
                        case "-":
                            self.i += 1
                            token = Token.DEC
                        case "=":
                            self.i += 1
                            token = Token.SUBASSIGN
                        case ">":
                            self.i += 1
                            token = Token.ARROW
                        case _:
                            token = Token.SUB

                case "/":
                    match self.__peek_next():
                        case "/":
                            self.consume_comment()
                        case "=":
                            self.i += 1
                            token = Token.DIVASSIGN
                        case _:
                            token = Token.DIV

                case "%":
                    if self.__peek_next() == "=":
                        self.i += 1
                        token = Token.MODASSIGN
                    else:
                        token = Token.MOD

                case "<":
                    match self.__peek_next():
                        case "=":
                            self.i += 1
                            token = Token.LE
                        case "<":
                            self.i += 1
                            token = Token.LSHIFT
                        case _:
                            token = Token.LT

                case ">":
                    match self.__peek_next():
                        case "=":
                            self.i += 1
                            token = Token.GE
                        case ">":
                            self.i += 1
                            token = Token.RSHIFT
                        case _:
                            token = Token.GT

                case "=":
                    if self.__peek_next() == "=":
                        self.i += 1
                        token = Token.EQ
                    else:
                        token = Token.ASSIGN

                case "&":
                    match self.__peek_next():
                        case "&":
                            self.i += 1
                            token = Token.AND
                        case "=":
                            self.i += 1
                            token = Token.LANDASSIGN
                        case _:
                            token = Token.LAND

                case "|":
                    match self.__peek_next():
                        case "|":
                            self.i += 1
                            token = Token.OR
                        case "=":
                            self.i += 1
                            token = Token.LORASSIGN
                        case _:
                            token = Token.LOR

                case "!":
                    if self.__peek_next() == "=":
                        self.i += 1
                        token = Token.NE
                    else:
                        token = Token.NOT

                case "?": token = Token.QUERY
                case ":": token = Token.COLON

                case "\"":
                    self.consume_string()
                    token = Token.STRING

                case "'":
                    self.consume_char()
                    token = Token.CHAR

                # TODO: handle preprocessor commands
                case "#":
                    _ = self.consume_line()

                case "":
                    token = Token.EOF

                case _:
                    if is_number(self.s[self.i]):
                        self.consume_number()
                        token = Token.NUMBER
                    elif is_alpha(self.s[self.i]):
                        s = self.consume_alphanumeric()
                        if s in keywords: token = keywords[s]
                        else: token = Token.IDENTIFIER
                    else:
                        raise Exception("Unexpected:", self.s[self.i])

            self.i += 1

        return token
