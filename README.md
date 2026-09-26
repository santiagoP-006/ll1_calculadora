# Calculadora Científica LL(1) con ANTLR4

Implementación de una gramática LL(1) en ANTLR4 para un lenguaje de calculadora científica.

---

## Características

- Operaciones aritméticas: suma, resta, multiplicación, división, módulo
- Funciones trigonométricas: `sin`, `cos`, `tan` (ángulos en grados)
- Valor absoluto: `abs`
- Asignación y uso de variables
- Análisis léxico, sintáctico y semántico completo
- Generación de árbol sintáctico visual en PDF
- Cálculo de conjuntos de Primeros, Siguientes y Predicción
- Detección de errores léxicos, sintácticos y semánticos

---

## Estructura del proyecto

```
ll1_calculadora/
├── antlr/
│   ├── CalcLL1.g4           # Gramática ANTLR4 LL(1)
│   ├── CalcLL1Lexer.py      # Generado por ANTLR4
│   ├── CalcLL1Parser.py     # Generado por ANTLR4
│   ├── CalcLL1Listener.py   # Generado por ANTLR4
│   ├── CalcLL1Visitor.py    # Generado por ANTLR4
│   ├── EvaluadorCalc.py     # Visitor semántico
│   └── main.py              # Punto de entrada
├── sets/
│   ├── primeros_siguientes.py   # Calculadora de conjuntos
│   └── gramatica_calc.txt       # Gramática en formato texto plano
├── tests/
│   └── pruebas.calc             # Casos de prueba
└── README.md
```

---

## Requisitos previos

### Sistema operativo
Ubuntu 22.04 o superior

### Java
```bash
sudo apt-get update
sudo apt-get install -y default-jdk
java -version
```

### Python 3
```bash
sudo apt-get install -y python3 python3-pip
python3 --version
```

### ANTLR4 JAR
```bash
wget https://www.antlr.org/download/antlr-4.13.2-complete.jar \
     -O ~/antlr-4.13.2-complete.jar
```

### Alias de ANTLR4 (opcional pero recomendado)
```bash
echo 'alias antlr4="java -jar ~/antlr-4.13.2-complete.jar"' >> ~/.bashrc
source ~/.bashrc
antlr4 --version
```

### Runtime de ANTLR4 para Python
```bash
pip3 install antlr4-python3-runtime==4.13.2
```

### Graphviz (para árbol visual)
```bash
pip3 install graphviz
sudo apt-get install -y graphviz
```

---

## Instalación

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd ll1_calculadora
```

### 2. Generar el parser y lexer con ANTLR4
```bash
cd antlr
java -jar ~/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener CalcLL1.g4
ls *.py
```

Deben aparecer: `CalcLL1Lexer.py`, `CalcLL1Parser.py`, `CalcLL1Listener.py`, `CalcLL1Visitor.py`

---

## Cómo ejecutar

### Analizar un archivo
```bash
cd antlr
python3 main.py ../tests/pruebas.calc
```

### Modo interactivo
```bash
cd antlr
python3 main.py
```
Escribe expresiones línea por línea. Deja una línea en blanco para terminar y ver el análisis completo.

### Calcular Primeros, Siguientes y Predicción
```bash
cd sets
python3 primeros_siguientes.py gramatica_calc.txt
```

---

## Sintaxis del lenguaje

### Operaciones aritméticas
```
3 + 5
10 - 4
6 * 7
20 / 4
17 % 5
```

### Precedencia de operadores
```
2 + 3 * 4        // Resultado: 14  (multiplicación primero)
(2 + 3) * 4      // Resultado: 20  (paréntesis primero)
```

### Asignación de variables
```
x = 10
y = 3
x + y
x * y - 2
```

### Funciones trigonométricas (ángulos en grados)
```
sin(30)          // 0.5
cos(60)          // 0.5
tan(45)          // 1.0
```

### Valor absoluto
```
abs(-15)         // 15
abs(-3 * 4)      // 12
```

### Negación unaria
```
-8 + 3           // -5
-x + y           // requiere x e y definidas previamente
```

### Comentarios
```
// Esto es un comentario de línea
```

---

## Salida del analizador

Al ejecutar `main.py` se muestran tres secciones:

```
=== ANALISIS LEXICO ===
  Token: NUMBER      |  Lexema: '3'   |  Linea: 1:0
  Token: PLUS        |  Lexema: '+'   |  Linea: 1:2
  ...

=== ARBOL DE ANALISIS SINTACTICO (texto) ===
  (programa (sentencia (expr ...)) ...)

=== ARBOL VISUAL ===
  [ARBOL] Generado: arbol_sintactico.pdf

=== ANALISIS SEMANTICO ===
  [SEMANTICO] Resultado: 8
  [SEMANTICO] Asignacion: x = 10
  ...
  [TABLA DE SIMBOLOS]
    x = 10
    y = 3
```

El árbol visual se abre automáticamente como PDF al finalizar el análisis.

---

## Ejemplos de errores detectados

### Error léxico — carácter no reconocido
```
5 @ 3
```
```
[ERROR SINTACTICO] Linea 1:2 - token recognition error at: '@'
[FALLO] Hay errores. No se ejecuta semantica.
```

### Error sintáctico — token inesperado
```
3 + * 5
```
```
[ERROR SINTACTICO] Linea 1:4 - extraneous input '*' expecting ...
[FALLO] Hay errores. No se ejecuta semantica.
```

### Error semántico — variable no definida
```
z + 5
```
```
[ERROR SEMANTICO] Variable no definida: 'z'
```

---

## Gramática LL(1)

La gramática usa **factorización por la izquierda** en `Sentencia` para eliminar
el conflicto con el token `id` y garantizar la propiedad LL(1).

```
Programa    →  Sentencia Programa  |  ε
Sentencia   →  id SentenciaP newline  |  ExprNoId newline
SentenciaP  →  assign Expr  |  TermP ExprP
Expr        →  Term ExprP
ExprP       →  plus Term ExprP  |  minus Term ExprP  |  ε
Term        →  Unary TermP
TermP       →  times Unary TermP  |  divide Unary TermP  |  mod Unary TermP  |  ε
Unary       →  minus Factor  |  Factor
Factor      →  sin ( Expr )  |  cos ( Expr )  |  tan ( Expr )  |  abs ( Expr )  |  PrimaryNoId
PrimaryNoId →  number  |  ( Expr )
ExprNoId    →  UnaryNoId TermP ExprP
UnaryNoId   →  minus Factor  |  FactorNoId
FactorNoId  →  sin ( Expr )  |  cos ( Expr )  |  tan ( Expr )  |  abs ( Expr )  |  PrimaryNoId
```

> **Nota:** La separación entre `Expr` (puede empezar con `id`) y `ExprNoId`
> (no puede) garantiza que los conjuntos de predicción de `Sentencia` sean
> completamente disjuntos, confirmando formalmente que la gramática es LL(1).

---

## herramientas utilizadas

| Herramienta | Versión | Uso |
|---|---|---|
| ANTLR4 | 4.13.2 | Generación del parser y lexer |
| Python | 3.x | Evaluador semántico y punto de entrada |
| antlr4-python3-runtime | 4.13.2 | Runtime de ANTLR4 para Python |
| Graphviz | latest | Visualización del árbol sintáctico |
| OpenJDK | 21 | Ejecución del JAR de ANTLR4 |

---

