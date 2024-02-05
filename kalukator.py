import sys

if len(sys.argv) != 4:
    print("Użycie: kalkulator.py <liczba_1> <operacja + - *> <liczba_2>")
    sys.exit(1)

liczba_1 = float(sys.argv[1])
operacja = sys.argv[2]
liczba_2 = float(sys.argv[3])

if operacja == "+":
    wynik = liczba_1 + liczba_2
elif operacja == "-":
    wynik = liczba_1 - liczba_2
elif operacja == "*":
    wynik = liczba_1 * liczba_2
else:
    print("Nieprawidłowa operacja. Dostępne operacje to +, - i *.")
    sys.exit(1)

with open("/tmp/wynik.txt", "w") as plik:
    plik.write(f"Wynik: {wynik}\n")

print(f"Wynik: {wynik}")
