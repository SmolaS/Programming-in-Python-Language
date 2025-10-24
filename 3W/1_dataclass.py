from dataclasses import dataclass
import json

@dataclass
class Osoba:
 imie: str
 nazwisko: str
 adres: str
 kod_pocztowy: str
 pesel: str

 def zapisz_do_json(self, nazwa_pliku):
  with open(nazwa_pliku, 'w') as plik:
   json.dump(self.__dict__, plik)

 @staticmethod
 def wczytaj_z_json(nazwa_pliku):
  with open(nazwa_pliku, 'r') as plik:
   dane = json.load(plik)
  return Osoba(**dane)

print("WPROWADZ DANE")
imie = input("Imię: ")
nazwisko = input("Nazwisko: ")
adres = input("Adres: ")
kod = input("Kod pocztowy: ")
pesel = input("PESEL: ")

osoba = Osoba(imie, nazwisko, adres, kod, pesel)
osoba.zapisz_do_json("osoba.json")

print("Dane zapisane do osoba.json")

nowa = Osoba.wczytaj_z_json("osoba.json")
print("Wczytano z pliku:", nowa)
