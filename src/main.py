from antlr4 import *
from generated.ArchDecisionLexer import ArchDecisionLexer
from generated.ArchDecisionParser import ArchDecisionParser
from src.ArchDecisionVisitorImpl import ArchDecisionInterpreter


def main():
    input_stream = FileStream("src/example.dsl")
    lexer = ArchDecisionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArchDecisionParser(stream)

    tree = parser.program()

    interpreter = ArchDecisionInterpreter()
    interpreter.visit(tree)


if __name__ == "__main__":
    main()
