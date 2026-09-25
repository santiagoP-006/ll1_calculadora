import math
from antlr4 import *
from CalcLL1Visitor import CalcLL1Visitor
from CalcLL1Parser import CalcLL1Parser


class EvaluadorCalc(CalcLL1Visitor):

    def __init__(self):
        self.variables = {}

    # ----------------------------------------------------------
    # programa: ejecuta cada sentencia
    # ----------------------------------------------------------
    def visitPrograma(self, ctx: CalcLL1Parser.ProgramaContext):
        resultados = []
        for sentencia in ctx.sentencia():
            r = self.visit(sentencia)
            if r is not None:
                resultados.append(r)
        return resultados

    # ----------------------------------------------------------
    # sentencia: id SentenciaP  →  delega en SentenciaP
    # ----------------------------------------------------------
    def visitSentenciaConId(self, ctx: CalcLL1Parser.SentenciaConIdContext):
        return self.visit(ctx.sentenciaP())

    # ----------------------------------------------------------
    # sentencia: expr sola (no empieza con id)
    # ----------------------------------------------------------
    def visitExpresionSola(self, ctx: CalcLL1Parser.ExpresionSolaContext):
        valor = self.visit(ctx.expr())
        print(f"  [SEMÁNTICO] Resultado: {valor}")
        return valor

    # ----------------------------------------------------------
    # sentenciaP: assign Expr  →  es asignación
    # ----------------------------------------------------------
    def visitEsAsignacion(self, ctx: CalcLL1Parser.EsAsignacionContext):
        nombre = ctx.parentCtx.ID().getText()
        valor  = self.visit(ctx.expr())
        self.variables[nombre] = valor
        print(f"  [SEMÁNTICO] Asignación: {nombre} = {valor}")
        return valor

    # ----------------------------------------------------------
    # sentenciaP: TermP ExprP  →  el id era inicio de expresión
    # ----------------------------------------------------------
    def visitEsExpresion(self, ctx: CalcLL1Parser.EsExpresionContext):
        nombre = ctx.parentCtx.ID().getText()
        if nombre not in self.variables:
            raise NameError(f"Variable no definida: '{nombre}'")
        base = self.variables[nombre]
        # Aplicar TermP sobre base
        base = self._evalTermP(ctx.termP(), base)
        # Aplicar ExprP sobre base
        base = self._evalExprP(ctx.exprP(), base)
        print(f"  [SEMÁNTICO] Resultado: {base}")
        return base

    # ----------------------------------------------------------
    # expr = term exprP
    # ----------------------------------------------------------
    def visitExpr(self, ctx: CalcLL1Parser.ExprContext):
        izq = self.visit(ctx.term())
        return self._evalExprP(ctx.exprP(), izq)

    def _evalExprP(self, ctx, acum):
        if ctx.getChildCount() == 0:
            return acum
        op   = ctx.getChild(0).getText()
        term = self.visit(ctx.term())
        if op == '+':
            acum += term
        else:
            acum -= term
        return self._evalExprP(ctx.exprP(), acum)

    # ----------------------------------------------------------
    # term = unary termP
    # ----------------------------------------------------------
    def visitTerm(self, ctx: CalcLL1Parser.TermContext):
        izq = self.visit(ctx.unary())
        return self._evalTermP(ctx.termP(), izq)

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
    # unary: negación o paso directo
    # ----------------------------------------------------------
    def visitNegacion(self, ctx: CalcLL1Parser.NegacionContext):
        return -self.visit(ctx.factor())

    def visitPasoFactor(self, ctx: CalcLL1Parser.PasoFactorContext):
        return self.visit(ctx.factor())

    # ----------------------------------------------------------
    # factor: funciones trigonométricas y abs
    # ----------------------------------------------------------
    def visitFuncSin(self, ctx: CalcLL1Parser.FuncSinContext):
        return math.sin(math.radians(self.visit(ctx.expr())))

    def visitFuncCos(self, ctx: CalcLL1Parser.FuncCosContext):
        return math.cos(math.radians(self.visit(ctx.expr())))

    def visitFuncTan(self, ctx: CalcLL1Parser.FuncTanContext):
        angulo = self.visit(ctx.expr())
        if abs(angulo % 180 - 90) < 1e-9:
            raise ValueError(f"tan({angulo}°) no está definida")
        return math.tan(math.radians(angulo))

    def visitFuncAbs(self, ctx: CalcLL1Parser.FuncAbsContext):
        return abs(self.visit(ctx.expr()))

    def visitPasoUnario(self, ctx: CalcLL1Parser.PasoUnarioContext):
        return self.visit(ctx.primary())

    # ----------------------------------------------------------
    # primary: número, variable, subexpresión
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
