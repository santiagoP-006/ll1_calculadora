// CalcLL1.g4 - Gramatica LL(1) para calculadora cientifica
// Operaciones: +, -, *, /, %, abs, sin, cos, tan
// Asignacion de variables

grammar CalcLL1;

// ============================================================
// REGLAS SINTACTICAS (Parser)
// ============================================================

programa
    : sentencia* EOF
    ;

sentencia
    : ID sentenciaP NEWLINE    # sentenciaConId
    | expr NEWLINE             # expresionSola
    ;

sentenciaP
    : ASSIGN expr              # esAsignacion
    | termP exprP              # esExpresion
    ;

expr
    : term exprP
    ;

exprP
    : PLUS  term exprP         # sumaP
    | MINUS term exprP         # restaP
    |                          # exprPVacio
    ;

term
    : unary termP
    ;

termP
    : TIMES  unary termP       # multP
    | DIVIDE unary termP       # divP
    | MOD    unary termP       # modP
    |                          # termPVacio
    ;

unary
    : MINUS factor             # negacion
    | factor                   # pasoFactor
    ;

factor
    : SIN    LPAREN expr RPAREN   # funcSin
    | COS    LPAREN expr RPAREN   # funcCos
    | TAN    LPAREN expr RPAREN   # funcTan
    | ABS    LPAREN expr RPAREN   # funcAbs
    | primary                     # pasoUnario
    ;

primary
    : NUMBER                   # numero
    | ID                       # variable
    | LPAREN expr RPAREN       # agrupacion
    ;

// ============================================================
// REGLAS LEXICAS (Lexer)
// ============================================================

SIN    : [sS][iI][nN] ;
COS    : [cC][oO][sS] ;
TAN    : [tT][aA][nN] ;
ABS    : [aA][bB][sS] ;

PLUS   : '+' ;
MINUS  : '-' ;
TIMES  : '*' ;
DIVIDE : '/' ;
MOD    : '%' ;
ASSIGN : '=' ;
LPAREN : '(' ;
RPAREN : ')' ;

NUMBER  : [0-9]+ ('.' [0-9]+)? ;
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NEWLINE : [\r\n]+ ;

WS      : [ \t]+ -> skip ;
COMMENT : '//' ~[\r\n]* [\r\n]+ -> skip ;
