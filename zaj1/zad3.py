from collections import Counter

czestotliwosc_polskich_liter = {
    'a': 10.5, 'e': 8.9, 'o': 8.5, 'i': 8.2, 'z': 5.8, 'n': 5.5, 'r': 5.1,
    's': 4.9, 'w': 4.8, 'c': 4.4, 't': 3.9, 'y': 3.9, 'k': 3.6, 'd': 3.3,
    'p': 3.1, 'm': 2.7, 'u': 2.5, 'j': 2.3, 'l': 2.3, 'b': 1.5, 'g': 1.4,
    'h': 1.1, 'f': 0.3, 'q': 0.2, 'v': 0.2, 'x': 0.2
}


def oblicz_czestotliwosc(tekst):
    tekst = tekst.lower()
    licznik = Counter([znak for znak in tekst if znak.isalpha()])
    dlugosc = sum(licznik.values())
    czestotliwosci = {znak: (liczba / dlugosc * 100) for znak, liczba in licznik.items()}
    return czestotliwosci


def szyfruj_cezara(tekst, klucz):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            kod_podstawowy = ord('a') if znak.islower() else ord('A')
            zaszyfrowany_znak = chr((ord(znak) - kod_podstawowy + klucz) % 26 + kod_podstawowy)
            zaszyfrowany_tekst += zaszyfrowany_znak
        else:
            zaszyfrowany_tekst += znak
    return zaszyfrowany_tekst


def deszyfruj_cezara(tekst, klucz):
    return szyfruj_cezara(tekst, -klucz)


def oblicz_odleglosc(czestotliwosc1, czestotliwosc2):
    odleglosc = 0
    for litera in czestotliwosc_polskich_liter:
        odleglosc += abs(czestotliwosc1.get(litera, 0) - czestotliwosc2.get(litera, 0))
    return odleglosc


def zlam_cezara(tekst, ile_propozycji):
    propozycje = []
    for klucz in range(26):
        odszyfrowany_tekst = deszyfruj_cezara(tekst, klucz)
        czestotliwosc_tekst = oblicz_czestotliwosc(odszyfrowany_tekst)
        odleglosc = oblicz_odleglosc(czestotliwosc_tekst, czestotliwosc_polskich_liter)
        propozycje.append((odszyfrowany_tekst, klucz, odleglosc))

    propozycje = sorted(propozycje, key=lambda x: x[2])

    return propozycje[:ile_propozycji]


tekst = input("Podaj zaszyfrowany tekst: ")
ile_propozycji = int(input("Podaj liczbę najbardziej prawdopodobnych kombinacji do wyświetlenia (do 10): "))

wyniki = zlam_cezara(tekst, ile_propozycji)
for i, (odszyfrowany, klucz, odleglosc) in enumerate(wyniki, 1):
    print(f"{i}. Klucz: {klucz}, Odległość: {odleglosc:.2f}, Tekst: {odszyfrowany}")
