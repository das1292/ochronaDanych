def przygotuj_klucz(tekst, klucz):
    klucz = klucz.lower()
    klucz_dopasowany = ""
    indeks = 0
    for znak in tekst:
        if znak.isalpha():
            klucz_dopasowany += klucz[indeks % len(klucz)]
            indeks += 1
        else:
            klucz_dopasowany += znak
    return klucz_dopasowany


def szyfruj_vigenere(tekst, klucz):
    klucz = przygotuj_klucz(tekst, klucz)
    zaszyfrowany_tekst = ""
    for i, znak in enumerate(tekst):
        if znak.isalpha():
            kod_podstawowy = ord('a') if znak.islower() else ord('A')
            przesuniecie = ord(klucz[i].lower()) - ord('a')
            zaszyfrowany_znak = chr((ord(znak) - kod_podstawowy + przesuniecie) % 26 + kod_podstawowy)
            zaszyfrowany_tekst += zaszyfrowany_znak
        else:
            zaszyfrowany_tekst += znak
    return zaszyfrowany_tekst


def odszyfruj_vigenere(tekst, klucz):
    klucz = przygotuj_klucz(tekst, klucz)
    odszyfrowany_tekst = ""
    for i, znak in enumerate(tekst):
        if znak.isalpha():
            kod_podstawowy = ord('a') if znak.islower() else ord('A')
            przesuniecie = ord(klucz[i].lower()) - ord('a')
            odszyfrowany_znak = chr((ord(znak) - kod_podstawowy - przesuniecie) % 26 + kod_podstawowy)
            odszyfrowany_tekst += odszyfrowany_znak
        else:
            odszyfrowany_tekst += znak
    return odszyfrowany_tekst


tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = input("Podaj klucz: ")

zaszyfrowany = szyfruj_vigenere(tekst, klucz)
odszyfrowany = odszyfruj_vigenere(zaszyfrowany, klucz)

print("Tekst zaszyfrowany:", zaszyfrowany)
print("Tekst odszyfrowany:", odszyfrowany)
