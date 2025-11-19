import sys
from antlr4 import *
from MatricesLexer import MatricesLexer
from MatricesParser import MatricesParser
from visitor import Analizador

def generar_gramatica_atributos():
    return Analizador()

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <archivo>")
        sys.exit(1)

    inp = FileStream(sys.argv[1])
    lexer = MatricesLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = MatricesParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Errores de sintaxis")
        sys.exit(1)

    motor = generar_gramatica_atributos()
    motor.visit(tree)

    if motor.errores:
        for e in motor.errores:
            print(e)
        sys.exit(1)
    else:
        print("¡Listo!")

if __name__ == "__main__":
    main()
