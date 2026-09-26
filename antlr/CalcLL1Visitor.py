# Generated from CalcLL1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcLL1Parser import CalcLL1Parser
else:
    from CalcLL1Parser import CalcLL1Parser

# This class defines a complete generic visitor for a parse tree produced by CalcLL1Parser.

class CalcLL1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcLL1Parser#programa.
    def visitPrograma(self, ctx:CalcLL1Parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#sentenciaConId.
    def visitSentenciaConId(self, ctx:CalcLL1Parser.SentenciaConIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#expresionSola.
    def visitExpresionSola(self, ctx:CalcLL1Parser.ExpresionSolaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#esAsignacion.
    def visitEsAsignacion(self, ctx:CalcLL1Parser.EsAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#esExpresion.
    def visitEsExpresion(self, ctx:CalcLL1Parser.EsExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#expr.
    def visitExpr(self, ctx:CalcLL1Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#sumaP.
    def visitSumaP(self, ctx:CalcLL1Parser.SumaPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#restaP.
    def visitRestaP(self, ctx:CalcLL1Parser.RestaPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#exprPVacio.
    def visitExprPVacio(self, ctx:CalcLL1Parser.ExprPVacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#term.
    def visitTerm(self, ctx:CalcLL1Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#multP.
    def visitMultP(self, ctx:CalcLL1Parser.MultPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#divP.
    def visitDivP(self, ctx:CalcLL1Parser.DivPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#modP.
    def visitModP(self, ctx:CalcLL1Parser.ModPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#termPVacio.
    def visitTermPVacio(self, ctx:CalcLL1Parser.TermPVacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#negacion.
    def visitNegacion(self, ctx:CalcLL1Parser.NegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#pasoFactor.
    def visitPasoFactor(self, ctx:CalcLL1Parser.PasoFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#funcSin.
    def visitFuncSin(self, ctx:CalcLL1Parser.FuncSinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#funcCos.
    def visitFuncCos(self, ctx:CalcLL1Parser.FuncCosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#funcTan.
    def visitFuncTan(self, ctx:CalcLL1Parser.FuncTanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#funcAbs.
    def visitFuncAbs(self, ctx:CalcLL1Parser.FuncAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#pasoUnario.
    def visitPasoUnario(self, ctx:CalcLL1Parser.PasoUnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#numero.
    def visitNumero(self, ctx:CalcLL1Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#variable.
    def visitVariable(self, ctx:CalcLL1Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcLL1Parser#agrupacion.
    def visitAgrupacion(self, ctx:CalcLL1Parser.AgrupacionContext):
        return self.visitChildren(ctx)



del CalcLL1Parser