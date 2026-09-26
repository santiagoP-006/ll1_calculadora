import sys
import math
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CalcLL1Lexer   import CalcLL1Lexer
from CalcLL1Parser  import CalcLL1Parser
from EvaluadorCalc  import EvaluadorCalc

try:
    from graphviz import Digraph
    GRAPHVIZ_OK = True
except ImportError:
    GRAPHVIZ_OK = False


# ── Listener de errores ──────────────────────────────────────
class ErroresCalc(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        err = f"[ERROR SINTACTICO] Linea {line}:{column} - {msg}"
        self.errores.append(err)
        print(err)


# ── Generador de árbol visual ────────────────────────────────
contador = [0]

def agregar_nodos(tree, parser, grafo, padre=None):
    nodo_id = str(contador[0])
    contador[0] += 1

    if isinstance(tree, TerminalNode):
        token    = tree.getSymbol()
        nombre   = CalcLL1Lexer.symbolicNames[token.type]
        etiqueta = f"{nombre}\n'{token.text}'"
        grafo.node(nodo_id, etiqueta, shape='ellipse',
                   style='filled', fillcolor='#AED6F1')
    else:
        nombre   = parser.ruleNames[tree.getRuleIndex()]
        etiqueta = nombre
        grafo.node(nodo_id, etiqueta, shape='box',
                   style='filled', fillcolor='#A9DFBF')

    if padre is not None:
        grafo.edge(padre, nodo_id)

    if not isinstance(tree, TerminalNode):
        for i in range(tree.getChildCount()):
            agregar_nodos(tree.getChild(i), parser, grafo, nodo_id)


def generar_arbol_visual(tree, parser, nombre_salida):
    if not GRAPHVIZ_OK:
        print("  [AVISO] graphviz no instalado - omitiendo arbol visual")
        return
    contador[0] = 0
    grafo = Digraph(comment='Arbol Sintactico', format='pdf')
    grafo.attr(rankdir='TB', size='14,10')
    grafo.attr('node', fontname='Helvetica', fontsize='10')
    agregar_nodos(tree, parser, grafo)
    grafo.render(nombre_salida, view=True, cleanup=True)
    print(f"  [ARBOL] Generado: {nombre_salida}.pdf")


# ── Función principal de análisis ───────────────────────────
def analizar(fuente: str, nombre_arbol: str = "arbol_sintactico"):
    stream = InputStream(fuente)

    # LEXICO
    lexer = CalcLL1Lexer(stream)
    lexer.removeErrorListeners()
    err_lex = ErroresCalc()
    lexer.addErrorListener(err_lex)

    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print("\n=== ANALISIS LEXICO ===")
    for tok in tokens.tokens:
        if tok.type == Token.EOF:
            break
        nombre = CalcLL1Lexer.symbolicNames[tok.type]
        print(f"  Token: {nombre:10s}  |  Lexema: '{tok.text}'"
              f"  |  Linea: {tok.line}:{tok.column}")

    # SINTACTICO
    parser = CalcLL1Parser(tokens)
    parser.removeErrorListeners()
    err_par = ErroresCalc()
    parser.addErrorListener(err_par)

    tree = parser.programa()

    print("\n=== ARBOL DE ANALISIS SINTACTICO (texto) ===")
    print(tree.toStringTree(recog=parser))

    if err_lex.errores or err_par.errores:
        print("\n[FALLO] Hay errores. No se ejecuta semantica.")
        return

    # ARBOL VISUAL
    print("\n=== ARBOL VISUAL ===")
    generar_arbol_visual(tree, parser, nombre_arbol)

    # SEMANTICO
    print("\n=== ANALISIS SEMANTICO ===")
    evaluador = EvaluadorCalc()
    try:
        evaluador.visitPrograma(tree)
        if evaluador.variables:
            print("\n  [TABLA DE SIMBOLOS]")
            for var, val in evaluador.variables.items():
                print(f"    {var} = {val}")
    except (ZeroDivisionError, ValueError, NameError) as ex:
        print(f"  [ERROR SEMANTICO] {ex}")


# ── Entrada ──────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        with open(sys.argv[1], encoding="utf-8") as f:
            fuente = f.read()
        nombre = sys.argv[1].replace("/","_").replace(".calc","")[-20:]
        print(f"[INFO] Analizando: {sys.argv[1]}")
        analizar(fuente, f"arbol_{nombre}")
    else:
        print("Calculadora LL(1) - escribe expresiones (linea vacia para terminar):")
        lineas = []
        try:
            while True:
                linea = input(">>> ")
                if linea == "":
                    break
                lineas.append(linea + "\n")
        except EOFError:
            pass
        if lineas:
            analizar("".join(lineas), "arbol_interactivo")
