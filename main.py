from typing import Callable, Tuple
import math

def frac(a: float, b: float) -> float: 
    """Dient zur übersichtlicheren Schreibweise von Brüchen"""
    if b == 0:
        raise Exception("Division durch 0")
    return a/b

def ordnung_modolu_multiplikativ(element: float, gruppe: float) -> float: 
    i = 1
    ergebnis = element % gruppe
    while ergebnis != 1:
        ergebnis = (ergebnis * element) % gruppe
        i = i + 1
    return i

def simpson_regel(f: Callable[[float], float], grenzen: Tuple[float, float]) -> float:
    a,b = grenzen
    return frac(b-a,6) * (f(a) + 4*f(frac(a+b,2)) + f(b))

def newton_regel(f: Callable[[float], float], grenzen: Tuple[float, float]) -> float:
    a, b = grenzen
    h = frac(b-a, 3) 
    return frac(b-a, 8) * (f(a) + 3*f(a + h) + 3*f(a + 2*h) + f(b))

def milne_regel(f: Callable[[float], float], grenzen: Tuple[float, float]) -> float:
    a, b = grenzen
    h = frac(b-a, 4) 
    return frac(b-a, 90) * (7*f(a) + 32*f(a+h) + 12*f(a+2*h) + 32*f(a+3*h) + 7*f(b))

def erweiterter_euklid(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return a, 1, 0  # Basisfall: ggT(a, 0) = a, x = 1, y = 0
    
    g, x1, y1 = erweiterter_euklid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def elemente_multiplikative_gruppe(n: float) -> list[float]:
    return [i for i in range(1, 14) if math.gcd(i, n) == 1]

def ordnung_multiplikative_gruppe(n: float) -> float:
    return len(elemente_multiplikative_gruppe(n))


if __name__ == "__main__":
    #Beispiele für Nutzung
    def f(x):
        return 1/(2*x + 1)
    
    print(f"Ergebnis der Simpsonregen bei 1/2x+1 mit den Grenzen 0, 1 -> {simpson_regel(f, [0,2])}")

    #Unterteilung des Intervals in [0,1] und [1,2]
    erstes_intervall, zweites_intervall = simpson_regel(f, [0,1]), simpson_regel(f, [1,2])
    addierte_intervalle = erstes_intervall + zweites_intervall
    print(f"Das Intervall in [0,1] und [1,2] aufgeteilt und dann addiert: {addierte_intervalle}")
    print(f"Mit der Newton Regel: {newton_regel(f, [0,2])}")
    print(f"Mit der Milne Regel: {milne_regel(f, [0,2])} ")



    gruppe = 17
    element1, element2 = 2, 3

    print(f"Ordnung von {element1} in der Gruppe {gruppe} ist {ordnung_modolu_multiplikativ(element1, gruppe)}")
    print(f"Ordnung von {element2} in der Gruppe {gruppe} ist {ordnung_modolu_multiplikativ(element2, gruppe)}")



    # Test für erweiterten euklidischen Algorithmus
    a, b = 56, 15
    ggt, x, y = erweiterter_euklid(a, b)
    print(f"Erweiterter Euklid für ({a}, {b}): ggT={ggt}, x={x}, y={y}")
    print(f"Überprüfung: {a}*{x} + {b}*{y} = {ggt}")

    #Test für Elemente einer multiplikativen Gruppe
    print(f"Die Elemente der multiplikativen Gruppe Z{14} sind {elemente_multiplikative_gruppe(14)} mit Ordnung {ordnung_multiplikative_gruppe(14)}")