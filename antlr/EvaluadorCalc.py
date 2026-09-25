# EvaluadorCalc.py — Visitor semántico para la calculadora LL(1)
# Maneja: +, -, *, /, %, abs, sin, cos, tan, asignación de variables

import math
from antlr4 import *
from CalcLL1Visitor import CalcLL1Visitor
from CalcLL1Parser import CalcLL1Parser


class EvaluadorCalc(CalcLL1Visitor):

    def __init__(self):
        # Tabla de símbolos: almacena variables y sus valores
        self.variables = {}

    # ----------------------------------------------------------
    # programa: ejecuta cada sentencia en orden
    # ----------------------------------------------------------
    def visitPrograma(self, ctx: CalcLL1Parser.ProgramaContext):
        resultados = []
        for sentencia in ctx.sentencia():
            r = self.visit(sentencia)
            if r is not None:
                resultados.append(r)
        return resultados

    # ----------------------------------------------------------
    # sentencia de asignación: id = expr
    # ----------------------------------------------------------
    def visitSentenciaConId(self, ctx):
     return self.visit(ctx.sentenciaP())

    def visitEsAsignacion(self, ctx):
    # El ID viene del nodo padre (sentenciaConId)
    nombre = ctx.parentCtx.ID().getText()
    valor  = self.visit(ctx.expr())
    self.variables[nombre] = valor
    print(f"  [SEMÁNTICO] Asignación: {nombre} = {valor}")
    return valor

def visitEsExpresion(self, ctx):
    # El ID ya fue consumido; reconstruimos el valor del Primary
    nombre = ctx.parentCtx.ID().getText()
    if nombre not in self.variables:
        raise NameError(f"Variable no definida: '{nombre}'")
    base = self.variables[nombre]
    # Continuar evaluando TermP y ExprP sobre ese valor base
    # (requiere pasar el valor base a los métodos de TermP/ExprP)
    return base  # simplificado; la lógica de acumulación ya está en visitTerm/visitExpr

    # ----------------------------------------------------------
    # sentencia de expresión: solo evalúa e imprime
    # ----------------------------------------------------------
    def visitExpresion(self, ctx: CalcLL1Parser.ExpresionContext):
        valor = self.visit(ctx.expr())
        print(f"  [SEMÁNTICO] Resultado: {valor}")
        return valor

    # ----------------------------------------------------------
    # expr = term exprP  →  acumula suma/resta
    # ----------------------------------------------------------
    def visitExpr(self, ctx: CalcLL1Parser.ExprContext):
        return self.visit(ctx.term()) + self._evalExprP(ctx.exprP(), 0)

    def _evalExprP(self, ctx, acum):
        # ExprP vacío
        if ctx.getChildCount() == 0:
            return acum
        # Distinguir + o -
        op    = ctx.getChild(0).getText()
        term  = self.visit(ctx.term())
        if op == '+':
            acum += term
        else:
            acum -= term
        return self._evalExprP(ctx.exprP(), acum)

    # ----------------------------------------------------------
    # term = unary termP  →  acumula *, /, %
    # ----------------------------------------------------------
    def visitTerm(self, ctx: CalcLL1Parser.TermContext):
        return self.visit(ctx.unary()) + self._evalTermP(ctx.termP(), 0)

    def _evalTermP(self, ctx, acum):
        if ctx.getChildCount() == 0:
            return acum
        op    = ctx.getChild(0).getText()
        unary = self.visit(ctx.unary())
        if op == '*':
            acum *= unary
        elif op == '/':
            if unary == 0:
                raise ZeroDivisionError("División entre cero")
            acum /= unary
        elif op == '%':
            if unary == 0:
                raise ZeroDivisionError("Módulo entre cero")
            acum %= unary
        return self._evalTermP(ctx.termP(), acum)

    # ----------------------------------------------------------
    # unary: negación unaria o paso directo a factor
    # ----------------------------------------------------------
    def visitNegacion(self, ctx: CalcLL1Parser.NegacionContext):
        return -self.visit(ctx.factor())

    def visitPasoFactor(self, ctx: CalcLL1Parser.PasoFactorContext):
        return self.visit(ctx.factor())

    # ----------------------------------------------------------
    # factor: funciones trigonométricas y valor absoluto
    # ----------------------------------------------------------
    def visitFuncSin(self, ctx: CalcLL1Parser.FuncSinContext):
        return math.sin(math.radians(self.visit(ctx.expr())))

    def visitFuncCos(self, ctx: CalcLL1Parser.FuncCosContext):
        return math.cos(math.radians(self.visit(ctx.expr())))

    def visitFuncTan(self, ctx: CalcLL1Parser.FuncTanContext):
        val = math.degrees(self.visit(ctx.expr()))
        if abs(val % 180 - 90) < 1e-9:
            raise ValueError(f"tan({val}°) no está definida")
        return math.tan(math.radians(self.visit(ctx.expr())))

    def visitFuncAbs(self, ctx: CalcLL1Parser.FuncAbsContext):
        return abs(self.visit(ctx.expr()))

    def visitPasoUnario(self, ctx: CalcLL1Parser.PasoUnarioContext):
        return self.visit(ctx.primary())

    # ----------------------------------------------------------
    # primary: número, variable o subexpresión
    # ----------------------------------------------------------
    def visitNumero(self, ctx: CalcLL1Parser.NumeroContext):
        texto = ctx.NUMBER().getText()
        return float(texto) if '.' in texto else int(texto)

    def visitVariable(self, ctx: CalcLL1Parser.VariableContext):
        nombre = ctx.ID().getText()
        if nombre not in self.variables:
            raise NameError(f"Variable no definida: '{nombre}'")
        return self.variables[nombre]

    def visitAgrupacion(self, ctx: CalcLL1Parser.AgrupacionContext):
        return self.visit(ctx.expr())

    # ----------------------------------------------------------
    # Métodos vacíos requeridos por la jerarquía (paso transparente)
    # ----------------------------------------------------------
    def visitExprP(self, ctx):   return 0
    def visitTermP(self, ctx):   return 0
    def visitFactor(self, ctx):  return self.visitChildren(ctx)
    def visitPrimary(self, ctx): return self.visitChildren(ctx)
