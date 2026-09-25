import sys

EPS = "ε"
FIN = "$"
EPSILONS = {"ε", "eps", "epsilon", "lambda", "λ"}


def leer_gramatica(ruta):
    reglas = []  # lista de (izquierda, [símbolos de la derecha])
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            linea = linea.replace("→", "->")
            izq, der = linea.split("->")
            izq = izq.strip()
            for alternativa in der.split("|"):
                simbolos = [s for s in alternativa.split() if s not in EPSILONS]
                reglas.append((izq, simbolos))
    return reglas

def primeros_de_secuencia(secuencia, primeros, no_terminales):
    resultado = set()
    for simbolo in secuencia:
        if simbolo not in no_terminales:      # terminal
            resultado.add(simbolo)
            return resultado
        resultado |= primeros[simbolo] - {EPS}
        if EPS not in primeros[simbolo]:
            return resultado
    resultado.add(EPS)                        # todos pueden ser vacíos
    return resultado


def calcular_primeros(reglas, no_terminales):
    primeros = {A: set() for A in no_terminales}
    cambio = True
    while cambio:
        cambio = False
        for izq, der in reglas:
            nuevos = primeros_de_secuencia(der, primeros, no_terminales)
            if not nuevos <= primeros[izq]:
                primeros[izq] |= nuevos
                cambio = True
    return primeros


def calcular_siguientes(reglas, no_terminales, inicial, primeros):
    siguientes = {A: set() for A in no_terminales}
    siguientes[inicial].add(FIN)
    cambio = True
    while cambio:
        cambio = False
        for izq, der in reglas:
            for i, simbolo in enumerate(der):
                if simbolo not in no_terminales:
                    continue
                resto = der[i + 1:]
                primeros_resto = primeros_de_secuencia(resto, primeros, no_terminales)
                nuevos = primeros_resto - {EPS}
                if EPS in primeros_resto:
                    nuevos |= siguientes[izq]
                if not nuevos <= siguientes[simbolo]:
                    siguientes[simbolo] |= nuevos
                    cambio = True
    return siguientes

def calcular_prediccion(reglas, no_terminales, primeros, siguientes):
    prediccion = []
    for izq, der in reglas:
        conjunto = primeros_de_secuencia(der, primeros, no_terminales)
        if EPS in conjunto:
            conjunto = (conjunto - {EPS}) | siguientes[izq]
        prediccion.append((izq, der, conjunto))
    return prediccion


def formato(conjunto):
    elementos = sorted(conjunto - {EPS, FIN})
    if FIN in conjunto:
        elementos.append(FIN)
    if EPS in conjunto:
        elementos.append(EPS)
    return "{ " + ", ".join(elementos) + " }"

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 primeros_siguientes.py <archivo_gramatica>")
        return

    reglas = leer_gramatica(sys.argv[1])
    no_terminales = []
    for izq, _ in reglas:
        if izq not in no_terminales:
            no_terminales.append(izq)
    inicial = no_terminales[0]

    primeros = calcular_primeros(reglas, no_terminales)
    siguientes = calcular_siguientes(reglas, no_terminales, inicial, primeros)
    prediccion = calcular_prediccion(reglas, no_terminales, primeros, siguientes)

    print("\n=== PRIMEROS ===")
    for A in no_terminales:
        print(f"PRIM({A}) = {formato(primeros[A])}")

    print("\n=== SIGUIENTES ===")
    for A in no_terminales:
        print(f"SIG({A}) = {formato(siguientes[A])}")

    print("\n=== PREDICCIÓN ===")
    for izq, der, conjunto in prediccion:
        derecha = " ".join(der) if der else EPS
        print(f"PRED({izq} -> {derecha}) = {formato(conjunto)}")

    print("\n=== ¿Es LL(1)? ===")
    es_ll1 = True
    for A in no_terminales:
        conjuntos = [c for izq, _, c in prediccion if izq == A]
        for i in range(len(conjuntos)):
            for j in range(i + 1, len(conjuntos)):
                comunes = conjuntos[i] & conjuntos[j]
                if comunes:
                    es_ll1 = False
                    print(f"Conflicto en {A}: {formato(comunes)}")
    print("Sí es LL(1)" if es_ll1 else "No es LL(1)")


if __name__ == "__main__":
    main()
