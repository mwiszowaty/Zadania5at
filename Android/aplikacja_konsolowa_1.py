class Film:
    def __init__(self, tytuł="", liczba_wypożyczeń=0):
        self._tytuł = tytuł
        self._liczba_wypożyczeń = liczba_wypożyczeń

    def setTytuł(self, nowy_tytuł):
        if len(nowy_tytuł) > 20:
            raise ValueError("Tytuł nie może przekraczać 20 znaków.")
        self._tytuł = nowy_tytuł
    def getTytuł(self):
        return self._tytuł
    def get_liczba_wypożyczeń(self):
        return self._liczba_wypożyczeń
    def inkrementacja(self):
        self._liczba_wypożyczeń += 1

film1 = Film()
film1.setTytuł("Minionki")
print(film1.getTytuł(), film1.get_liczba_wypożyczeń())
film1.inkrementacja()
print(film1.getTytuł(), film1.get_liczba_wypożyczeń())