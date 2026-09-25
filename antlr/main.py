# main.py — Punto de entrada de la calculadora LL(1)
# Uso: python3 main.py <archivo_entrada>
#      python3 main.py              (modo interactivo)

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CalcLL1Lexer  import CalcLL1Lexer
from CalcLL1Parser import CalcLL1Parser
from EvaluadorCalc import EvaluadorCalc


# ──────────────────────────────────────────────
# Listener de errores personalizado
# ──────────────────────────────────────────────
class ErroresCalc(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        err = f"[ERROR SINTÁCTICO] Línea {line}:{column} — {msg}"
        self.errores.append(err)
        print(err)


# ──────────────────────────────────────────────
# Función principal de análisis
# ──────────────────────────────────────────────
def analizar(fuente: str):
    input_stream = InputStream(fuente)

    # --- LÉXICO ---
    lexer   = CalcLL1Lexer(input_stream)
    lexer.removeErrorListeners()
    err_lexer = ErroresCalc()
    lexer.addErrorListener(err_lexer)

    tokens  = CommonTokenStream(lexer)
    tokens.fill()

    # Mostrar tabla de tokens
    print("\n=== ANÁLISIS LÉXICO ===")
    for tok in tokens.tokens:
        if tok.type == Token.EOF:
            break
        nombre = CalcLL1Lexer.symbolicNames[tok.type]
        print(f"  Token: {nombre:10s}  |  Lexema: '{tok.text}'  "
              f"|  Línea: {tok.line}:{tok.column}")

    # --- SINTÁCTICO ---
    parser  = CalcLL1Parser(tokens)
    parser.removeErrorListeners()
    err_parser = ErroresCalc()
    parser.addErrorListener(err_parser)

    tree = parser.programa()

    print("\n=== ÁRBOL DE ANÁLISIS SINTÁCTICO ===")
    print(tree.toStringTree(recog=parser))

    if err_lexer.errores or err_parser.errores:
        print("\n[FALLO] Se encontraron errores. No se ejecuta semántica.")
        return

    # --- SEMÁNTICO ---
    print("\n=== ANÁLISIS SEMÁNTICO ===")
    evaluador = EvaluadorCalc()
    try:
        evaluador.visitPrograma(tree)
        if evaluador.variables:
            print("\n  [TABLA DE SÍMBOLOS]")
            for var, val in evaluador.variables.items():
                print(f"    {var} = {val}")
    except (ZeroDivisionError, ValueError, NameError) as ex:
        print(f"  [ERROR SEMÁNTICO] {ex}")


# ──────────────────────────────────────────────
# Entrada: archivo o interactivo
# ──────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1], encoding="utf-8") as f:
            fuente = f.read()
        print(f"[INFO] Analizando archivo: {sys.argv[1]}")
        analizar(fuente)
    else:
        print("Calculadora LL(1) — modo interactivo (Ctrl+D para salir)")
        print("Escribe expresiones y termina con Enter.\n")
        lineas = []
        try:
            while True:
                lineas.append(input(">>> ") + "\n")
        except EOFError:
            pass
        analizar("".join(lineas))
