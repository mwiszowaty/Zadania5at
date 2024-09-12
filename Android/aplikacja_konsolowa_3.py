class Notatka:
    licznik = 0
    def __init__(self, tytul="", notatka=""):
        Notatka.licznik += 1
        self.__id = Notatka.licznik
        self._tytul = tytul
        self._notatka = notatka

    def wyswietl(self):
        return f"Tytul: {self._tytul}, Notatka: {self._notatka}"

    def diagnoza(self):
        return f"Id: {self.__id} ; Tytul: {self._tytul} ; Notatka: {self._notatka}"

notatka1 = Notatka("okok","ahaokok")
notatka2 = Notatka("damistrz","monster")
print(notatka2.diagnoza())
print(notatka1.diagnoza())
print(notatka1.wyswietl())
print(notatka2.wyswietl())