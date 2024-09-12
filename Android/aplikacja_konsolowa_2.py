class Osoba:
    liczbaInstancji = 0
    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczbaInstancji += 1

    def kopiowanie(self, o):
        return Osoba(o.__id, o.__imie)

osoba1 = Osoba(1, "Jan")
print(Osoba.liczbaInstancji)
osoba2 = osoba1.kopiowanie(osoba1)
print(osoba1)
print(osoba2)