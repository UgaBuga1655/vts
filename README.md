# vts
Instrukcja obsługi robotobiasza

Żeby uruchomić program należy wejść do folderu z plikem robo_tobiasz.py wpisać w terminal:
```
python3 robo_tobiasz.py ŚCIEŻKA_DO_PLIKU
```

Na przykład
```
python3 robo_tobiasz.py tabele/2lo
```

Format pliku:
```
IMIĘ NAZWISKO ROZSZERZENIE ROZSZERZENIE ROZSZERZENIE
IMIĘ NAZWISKO ROZSZERZENIE ROZSZERZENIE
IMIĘ NAZWISKO ROZSZERZENIE ROZSZERZENIE ROZSZERZENIE ROZSZERZENIE
```
Imiona i nazwiska nie mają żadnego znaczenia dla działania programu, służą jedynie czytelności pliku dla człowieka, nie należy ich jednak pomijać.
Rozszerzeń może być dowolna liczba, można zapisywać je jako skróty (mat pol ang) lub pełnymi nazwami (matematyka język-polski język_angielski), byle bez spacji ani innych białych znaków i jednolicie w całym pliku.
Imię, nazwisko i rozszerzenia muszą być oddzielone białymi znakami, najlepiej spacjami lub tabami.

Na przykład:
```
Andrzej     Babinicz  pol ang his
Aleksandra  Billewicz wos his
Damian      Kiemlicz  mat fiz inf che
```
Program zwróci wszystkie możliwe kliki przedmiotów posortowane alfabetycznie. Żeby zapisać je w pliku należy wpisać:
```
python3 robo_tobiasz.py ŚCIEŻKA_DO_PLIKU > NAZWA_PLIKU_WYJŚCIOWEGO
```

Na przykład:
```
python3 robo_tobiasz.py 2lo > 2loroz
```

Żeby sprawdzić, czy jakaś kombinacja rozszerzeń jest możliwa:
```
grep "ROZSZERZENIE.*ROZSZERZENIE" NAZWA_PLIKU_WYJŚCIOWEGO
```
Przy czym rozszerzeń może być dowolnie dużo, muszą jednak być ułożone alfabetycznie rosnąco i być rozdzielone przez znaki “.*” (kropka i asterix)i.

Na przykład:
```
grep "fiz.*geo.*hst" 2loroz
```

Sprawdza, czy fizyka, geografia i historia sztuki mogą odbywać się naraz.

Program zwróci wszystkie możliwe kombinacje zawierające przedmioty z zapytania. Jeśli nie zwróci nic, to oznacza, że taka kombinacja nie jest możliwa i istnieje uczeń, który rozszerza przynajmniej 2 z nich.
