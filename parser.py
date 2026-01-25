from lexer import Lexer, Token, is_type

class FunctionParser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

    def parse_fundef(self) -> list[Token]:
        tokens = []

        while (t := self.lexer.consume()) != Token.LPAREN and t != Token.EOF:
            pass

        while (t := self.lexer.consume()) != Token.RPAREN and t != Token.EOF:
            tokens.append(t)

        if self.lexer.consume() != Token.LBRACE: return tokens

        braces = 1
        while braces:
            match self.lexer.consume():
                case Token.LBRACE: braces += 1
                case Token.RBRACE: braces -= 1
                case Token.EOF: raise Exception("Unexpected EOF")
                case token:
                    tokens.append(token)

        return tokens

    def parse_fundefs(self) -> list[list[Token]]:
        fundefs = []
        while self.lexer.peek() != Token.EOF:
            fundefs.append(self.parse_fundef())

        return fundefs
