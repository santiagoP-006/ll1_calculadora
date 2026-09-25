// CalcLL1.g4 — Gramática LL(1) para calculadora científica
// Operaciones: +, -, *, /, %, abs, sin, cos, tan
// Asignación de variables
// Santiago — Lenguajes de Programación 2026-02

grammar CalcLL1;

//REGLAS SINTÁCTICAS (Parser)

programa
    : sentencia* EOF
    ;

sentencia
    : ID sentenciaP NEWLINE   # sentenciaConId
    | expr NEWLINE             # expresionSola
    ;

sentenciaP
    : ASSIGN expr # esAsignacion
    | expr NEWLINE # esExpresion

// Nivel 1: suma y resta  (menor precedencia)
expr
    : term exprP
    ;

exprP
    : PLUS  term exprP         # sumaP
    | MINUS term exprP         # restaP
    |                          # exprPVacio
    ;

// Nivel 2: multiplicación, división, módulo
term
    : unary termP
    ;

termP
    : TIMES  unary termP       # multP
    | DIVIDE unary termP       # divP
    | MOD    unary termP       # modP
    |                          # termPVacio
    ;

// Nivel 3: negación unaria
unary
    : MINUS factor             # negacion
    | factor                   # pasoFactor
    ;

// Nivel 4: funciones y valor absoluto
factor
    : SIN    LPAREN expr RPAREN   # funcSin
    | COS    LPAREN expr RPAREN   # funcCos
    | TAN    LPAREN expr RPAREN   # funcTan
    | ABS    LPAREN expr RPAREN   # funcAbs
    | primary                     # pasoUnario
    ;

// Nivel 5: átomos  (mayor precedencia)
primary
    : NUMBER                   # numero
    | ID                       # variable
    | LPAREN expr RPAREN       # agrupacion
    ;

// ============================================================
// REGLAS LÉXICAS (Lexer)
// ============================================================

// Palabras reservadas (funciones trigonométricas y abs)
SIN    : 'sin' | 'SIN' ;
COS    : 'cos' | 'COS' ;
TAN    : 'tan' | 'TAN' ;
ABS    : 'abs' | 'ABS' ;

// Operadores aritméticos
PLUS   : '+' ;
MINUS  : '-' ;
TIMES  : '*' ;
DIVIDE : '/' ;
MOD    : '%' ;

// Asignación
ASSIGN : '=' ;

// Delimitadores
LPAREN : '(' ;
RPAREN : ')' ;

// Literales numéricos: enteros y decimales
NUMBER : [0-9]+ ('.' [0-9]+)? ;

// Identificadores de variables: letra seguida de letras/dígitos
ID : [a-zA-Z_][a-zA-Z_0-9]* ;

// Fin de línea lógico
NEWLINE : [\r\n]+ ;

// Ignorar espacios y tabulaciones
WS : [ \t]+ -> skip ;

// Ignorar comentarios de línea
COMMENT : '//' ~[\r\n]* -> skip ;
