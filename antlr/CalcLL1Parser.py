# Generated from CalcLL1.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,3,2,
        43,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,57,8,
        4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,75,8,6,1,7,1,7,1,7,3,7,80,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,103,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,111,8,9,1,9,0,0,10,0,2,4,6,8,10,
        12,14,16,18,0,0,117,0,23,1,0,0,0,2,35,1,0,0,0,4,42,1,0,0,0,6,44,
        1,0,0,0,8,56,1,0,0,0,10,58,1,0,0,0,12,74,1,0,0,0,14,79,1,0,0,0,16,
        102,1,0,0,0,18,110,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,
        0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,
        5,0,0,1,27,1,1,0,0,0,28,29,5,14,0,0,29,30,3,4,2,0,30,31,5,15,0,0,
        31,36,1,0,0,0,32,33,3,6,3,0,33,34,5,15,0,0,34,36,1,0,0,0,35,28,1,
        0,0,0,35,32,1,0,0,0,36,3,1,0,0,0,37,38,5,10,0,0,38,43,3,6,3,0,39,
        40,3,6,3,0,40,41,5,15,0,0,41,43,1,0,0,0,42,37,1,0,0,0,42,39,1,0,
        0,0,43,5,1,0,0,0,44,45,3,10,5,0,45,46,3,8,4,0,46,7,1,0,0,0,47,48,
        5,5,0,0,48,49,3,10,5,0,49,50,3,8,4,0,50,57,1,0,0,0,51,52,5,6,0,0,
        52,53,3,10,5,0,53,54,3,8,4,0,54,57,1,0,0,0,55,57,1,0,0,0,56,47,1,
        0,0,0,56,51,1,0,0,0,56,55,1,0,0,0,57,9,1,0,0,0,58,59,3,14,7,0,59,
        60,3,12,6,0,60,11,1,0,0,0,61,62,5,7,0,0,62,63,3,14,7,0,63,64,3,12,
        6,0,64,75,1,0,0,0,65,66,5,8,0,0,66,67,3,14,7,0,67,68,3,12,6,0,68,
        75,1,0,0,0,69,70,5,9,0,0,70,71,3,14,7,0,71,72,3,12,6,0,72,75,1,0,
        0,0,73,75,1,0,0,0,74,61,1,0,0,0,74,65,1,0,0,0,74,69,1,0,0,0,74,73,
        1,0,0,0,75,13,1,0,0,0,76,77,5,6,0,0,77,80,3,16,8,0,78,80,3,16,8,
        0,79,76,1,0,0,0,79,78,1,0,0,0,80,15,1,0,0,0,81,82,5,1,0,0,82,83,
        5,11,0,0,83,84,3,6,3,0,84,85,5,12,0,0,85,103,1,0,0,0,86,87,5,2,0,
        0,87,88,5,11,0,0,88,89,3,6,3,0,89,90,5,12,0,0,90,103,1,0,0,0,91,
        92,5,3,0,0,92,93,5,11,0,0,93,94,3,6,3,0,94,95,5,12,0,0,95,103,1,
        0,0,0,96,97,5,4,0,0,97,98,5,11,0,0,98,99,3,6,3,0,99,100,5,12,0,0,
        100,103,1,0,0,0,101,103,3,18,9,0,102,81,1,0,0,0,102,86,1,0,0,0,102,
        91,1,0,0,0,102,96,1,0,0,0,102,101,1,0,0,0,103,17,1,0,0,0,104,111,
        5,13,0,0,105,111,5,14,0,0,106,107,5,11,0,0,107,108,3,6,3,0,108,109,
        5,12,0,0,109,111,1,0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,
        1,0,0,0,111,19,1,0,0,0,8,23,35,42,56,74,79,102,110
    ]

class CalcLL1Parser ( Parser ):

    grammarFileName = "CalcLL1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SIN", "COS", "TAN", "ABS", "PLUS", "MINUS", 
                      "TIMES", "DIVIDE", "MOD", "ASSIGN", "LPAREN", "RPAREN", 
                      "NUMBER", "ID", "NEWLINE", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_sentenciaP = 2
    RULE_expr = 3
    RULE_exprP = 4
    RULE_term = 5
    RULE_termP = 6
    RULE_unary = 7
    RULE_factor = 8
    RULE_primary = 9

    ruleNames =  [ "programa", "sentencia", "sentenciaP", "expr", "exprP", 
                   "term", "termP", "unary", "factor", "primary" ]

    EOF = Token.EOF
    SIN=1
    COS=2
    TAN=3
    ABS=4
    PLUS=5
    MINUS=6
    TIMES=7
    DIVIDE=8
    MOD=9
    ASSIGN=10
    LPAREN=11
    RPAREN=12
    NUMBER=13
    ID=14
    NEWLINE=15
    WS=16
    COMMENT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalcLL1Parser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcLL1Parser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CalcLL1Parser.SentenciaContext,i)


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = CalcLL1Parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26718) != 0):
                self.state = 20
                self.sentencia()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(CalcLL1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_sentencia

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SentenciaConIdContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalcLL1Parser.ID, 0)
        def sentenciaP(self):
            return self.getTypedRuleContext(CalcLL1Parser.SentenciaPContext,0)

        def NEWLINE(self):
            return self.getToken(CalcLL1Parser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaConId" ):
                listener.enterSentenciaConId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaConId" ):
                listener.exitSentenciaConId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaConId" ):
                return visitor.visitSentenciaConId(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionSolaContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(CalcLL1Parser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionSola" ):
                listener.enterExpresionSola(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionSola" ):
                listener.exitExpresionSola(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionSola" ):
                return visitor.visitExpresionSola(self)
            else:
                return visitor.visitChildren(self)



    def sentencia(self):

        localctx = CalcLL1Parser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CalcLL1Parser.SentenciaConIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(CalcLL1Parser.ID)
                self.state = 29
                self.sentenciaP()
                self.state = 30
                self.match(CalcLL1Parser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = CalcLL1Parser.ExpresionSolaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.expr()
                self.state = 33
                self.match(CalcLL1Parser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_sentenciaP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EsExpresionContext(SentenciaPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.SentenciaPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(CalcLL1Parser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEsExpresion" ):
                listener.enterEsExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEsExpresion" ):
                listener.exitEsExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEsExpresion" ):
                return visitor.visitEsExpresion(self)
            else:
                return visitor.visitChildren(self)


    class EsAsignacionContext(SentenciaPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.SentenciaPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(CalcLL1Parser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEsAsignacion" ):
                listener.enterEsAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEsAsignacion" ):
                listener.exitEsAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEsAsignacion" ):
                return visitor.visitEsAsignacion(self)
            else:
                return visitor.visitChildren(self)



    def sentenciaP(self):

        localctx = CalcLL1Parser.SentenciaPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentenciaP)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = CalcLL1Parser.EsAsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(CalcLL1Parser.ASSIGN)
                self.state = 38
                self.expr()
                pass
            elif token in [1, 2, 3, 4, 6, 11, 13, 14]:
                localctx = CalcLL1Parser.EsExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.expr()
                self.state = 40
                self.match(CalcLL1Parser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(CalcLL1Parser.TermContext,0)


        def exprP(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprPContext,0)


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CalcLL1Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.term()
            self.state = 45
            self.exprP()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_exprP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SumaPContext(ExprPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.ExprPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(CalcLL1Parser.PLUS, 0)
        def term(self):
            return self.getTypedRuleContext(CalcLL1Parser.TermContext,0)

        def exprP(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaP" ):
                listener.enterSumaP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaP" ):
                listener.exitSumaP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaP" ):
                return visitor.visitSumaP(self)
            else:
                return visitor.visitChildren(self)


    class ExprPVacioContext(ExprPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.ExprPContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPVacio" ):
                listener.enterExprPVacio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPVacio" ):
                listener.exitExprPVacio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPVacio" ):
                return visitor.visitExprPVacio(self)
            else:
                return visitor.visitChildren(self)


    class RestaPContext(ExprPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.ExprPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(CalcLL1Parser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(CalcLL1Parser.TermContext,0)

        def exprP(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestaP" ):
                listener.enterRestaP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestaP" ):
                listener.exitRestaP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestaP" ):
                return visitor.visitRestaP(self)
            else:
                return visitor.visitChildren(self)



    def exprP(self):

        localctx = CalcLL1Parser.ExprPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exprP)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = CalcLL1Parser.SumaPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(CalcLL1Parser.PLUS)
                self.state = 48
                self.term()
                self.state = 49
                self.exprP()
                pass
            elif token in [6]:
                localctx = CalcLL1Parser.RestaPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(CalcLL1Parser.MINUS)
                self.state = 52
                self.term()
                self.state = 53
                self.exprP()
                pass
            elif token in [12, 15]:
                localctx = CalcLL1Parser.ExprPVacioContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(CalcLL1Parser.UnaryContext,0)


        def termP(self):
            return self.getTypedRuleContext(CalcLL1Parser.TermPContext,0)


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = CalcLL1Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.unary()
            self.state = 59
            self.termP()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_termP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivPContext(TermPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.TermPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIVIDE(self):
            return self.getToken(CalcLL1Parser.DIVIDE, 0)
        def unary(self):
            return self.getTypedRuleContext(CalcLL1Parser.UnaryContext,0)

        def termP(self):
            return self.getTypedRuleContext(CalcLL1Parser.TermPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivP" ):
                listener.enterDivP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivP" ):
                listener.exitDivP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivP" ):
                return visitor.visitDivP(self)
            else:
                return visitor.visitChildren(self)


    class MultPContext(TermPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.TermPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIMES(self):
            return self.getToken(CalcLL1Parser.TIMES, 0)
        def unary(self):
            return self.getTypedRuleContext(CalcLL1Parser.UnaryContext,0)

        def termP(self):
            return self.getTypedRuleContext(CalcLL1Parser.TermPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultP" ):
                listener.enterMultP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultP" ):
                listener.exitMultP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultP" ):
                return visitor.visitMultP(self)
            else:
                return visitor.visitChildren(self)


    class TermPVacioContext(TermPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.TermPContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermPVacio" ):
                listener.enterTermPVacio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermPVacio" ):
                listener.exitTermPVacio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermPVacio" ):
                return visitor.visitTermPVacio(self)
            else:
                return visitor.visitChildren(self)


    class ModPContext(TermPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.TermPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOD(self):
            return self.getToken(CalcLL1Parser.MOD, 0)
        def unary(self):
            return self.getTypedRuleContext(CalcLL1Parser.UnaryContext,0)

        def termP(self):
            return self.getTypedRuleContext(CalcLL1Parser.TermPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModP" ):
                listener.enterModP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModP" ):
                listener.exitModP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModP" ):
                return visitor.visitModP(self)
            else:
                return visitor.visitChildren(self)



    def termP(self):

        localctx = CalcLL1Parser.TermPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_termP)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = CalcLL1Parser.MultPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(CalcLL1Parser.TIMES)
                self.state = 62
                self.unary()
                self.state = 63
                self.termP()
                pass
            elif token in [8]:
                localctx = CalcLL1Parser.DivPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(CalcLL1Parser.DIVIDE)
                self.state = 66
                self.unary()
                self.state = 67
                self.termP()
                pass
            elif token in [9]:
                localctx = CalcLL1Parser.ModPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(CalcLL1Parser.MOD)
                self.state = 70
                self.unary()
                self.state = 71
                self.termP()
                pass
            elif token in [5, 6, 12, 15]:
                localctx = CalcLL1Parser.TermPVacioContext(self, localctx)
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_unary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NegacionContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(CalcLL1Parser.MINUS, 0)
        def factor(self):
            return self.getTypedRuleContext(CalcLL1Parser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegacion" ):
                listener.enterNegacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegacion" ):
                listener.exitNegacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegacion" ):
                return visitor.visitNegacion(self)
            else:
                return visitor.visitChildren(self)


    class PasoFactorContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(CalcLL1Parser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPasoFactor" ):
                listener.enterPasoFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPasoFactor" ):
                listener.exitPasoFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPasoFactor" ):
                return visitor.visitPasoFactor(self)
            else:
                return visitor.visitChildren(self)



    def unary(self):

        localctx = CalcLL1Parser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_unary)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = CalcLL1Parser.NegacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(CalcLL1Parser.MINUS)
                self.state = 77
                self.factor()
                pass
            elif token in [1, 2, 3, 4, 11, 13, 14]:
                localctx = CalcLL1Parser.PasoFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncAbsContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABS(self):
            return self.getToken(CalcLL1Parser.ABS, 0)
        def LPAREN(self):
            return self.getToken(CalcLL1Parser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CalcLL1Parser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncAbs" ):
                listener.enterFuncAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncAbs" ):
                listener.exitFuncAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncAbs" ):
                return visitor.visitFuncAbs(self)
            else:
                return visitor.visitChildren(self)


    class FuncTanContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(CalcLL1Parser.TAN, 0)
        def LPAREN(self):
            return self.getToken(CalcLL1Parser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CalcLL1Parser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncTan" ):
                listener.enterFuncTan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncTan" ):
                listener.exitFuncTan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncTan" ):
                return visitor.visitFuncTan(self)
            else:
                return visitor.visitChildren(self)


    class FuncSinContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(CalcLL1Parser.SIN, 0)
        def LPAREN(self):
            return self.getToken(CalcLL1Parser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CalcLL1Parser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncSin" ):
                listener.enterFuncSin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncSin" ):
                listener.exitFuncSin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncSin" ):
                return visitor.visitFuncSin(self)
            else:
                return visitor.visitChildren(self)


    class FuncCosContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(CalcLL1Parser.COS, 0)
        def LPAREN(self):
            return self.getToken(CalcLL1Parser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CalcLL1Parser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCos" ):
                listener.enterFuncCos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCos" ):
                listener.exitFuncCos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCos" ):
                return visitor.visitFuncCos(self)
            else:
                return visitor.visitChildren(self)


    class PasoUnarioContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(CalcLL1Parser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPasoUnario" ):
                listener.enterPasoUnario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPasoUnario" ):
                listener.exitPasoUnario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPasoUnario" ):
                return visitor.visitPasoUnario(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = CalcLL1Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CalcLL1Parser.FuncSinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(CalcLL1Parser.SIN)
                self.state = 82
                self.match(CalcLL1Parser.LPAREN)
                self.state = 83
                self.expr()
                self.state = 84
                self.match(CalcLL1Parser.RPAREN)
                pass
            elif token in [2]:
                localctx = CalcLL1Parser.FuncCosContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(CalcLL1Parser.COS)
                self.state = 87
                self.match(CalcLL1Parser.LPAREN)
                self.state = 88
                self.expr()
                self.state = 89
                self.match(CalcLL1Parser.RPAREN)
                pass
            elif token in [3]:
                localctx = CalcLL1Parser.FuncTanContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(CalcLL1Parser.TAN)
                self.state = 92
                self.match(CalcLL1Parser.LPAREN)
                self.state = 93
                self.expr()
                self.state = 94
                self.match(CalcLL1Parser.RPAREN)
                pass
            elif token in [4]:
                localctx = CalcLL1Parser.FuncAbsContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(CalcLL1Parser.ABS)
                self.state = 97
                self.match(CalcLL1Parser.LPAREN)
                self.state = 98
                self.expr()
                self.state = 99
                self.match(CalcLL1Parser.RPAREN)
                pass
            elif token in [11, 13, 14]:
                localctx = CalcLL1Parser.PasoUnarioContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcLL1Parser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AgrupacionContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CalcLL1Parser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcLL1Parser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CalcLL1Parser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgrupacion" ):
                listener.enterAgrupacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgrupacion" ):
                listener.exitAgrupacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgrupacion" ):
                return visitor.visitAgrupacion(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CalcLL1Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcLL1Parser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalcLL1Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = CalcLL1Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primary)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = CalcLL1Parser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(CalcLL1Parser.NUMBER)
                pass
            elif token in [14]:
                localctx = CalcLL1Parser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(CalcLL1Parser.ID)
                pass
            elif token in [11]:
                localctx = CalcLL1Parser.AgrupacionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(CalcLL1Parser.LPAREN)
                self.state = 107
                self.expr()
                self.state = 108
                self.match(CalcLL1Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





