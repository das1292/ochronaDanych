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


def odszyfruj_cezara(tekst, klucz):
    return szyfruj_cezara(tekst, -klucz)


tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = int(input("Podaj klucz (liczbę przesunięć): "))

zaszyfrowany = szyfruj_cezara(tekst, klucz)
odszyfrowany = odszyfruj_cezara(zaszyfrowany, klucz)

print("Tekst zaszyfrowany:", zaszyfrowany)
print("Tekst odszyfrowany:", odszyfrowany)
