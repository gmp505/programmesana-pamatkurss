Koda lauzējs: AI Efektivitāte

# Projekta apraksts
Šajā projektā izveidoju Python spēli, kurā dators mēģina uzminēt spēlētāja iedomāto skaitli no 1 līdz 100.

Dators izmanto binārās meklēšanas algoritmu.

# Kā palaist programmu?
1. Atver projektu VS Code.
2. Atver termināli.
3. Ieraksti:

python 76.py

# Kā darbojas algoritms?
Binārā meklēšana katrā solī sadala iespējamo skaitļu diapazonu uz pusēm.

Ja skaitlis ir lielāks par datora minējumu, apakšējā robeža tiek palielināta.

Ja skaitlis ir mazāks, augšējā robeža tiek samazināta.


## Efektivitātes analīze

Binārās meklēšanas sarežģītība ir O(log n).

100 skaitļiem nepieciešami ne vairāk kā 7 minējumi.

1000 skaitļiem nepieciešami ne vairāk kā 10 minējumi.

Salīdzinājumam, lineārā meklēšana sliktākajā gadījumā pārbaudītu visus 100 vai 1000 skaitļus.

## Testēšanas rezultāti

| Skaitlis | Minējumu skaits |
| 73 | 6 |
| 25 | 2 |
| 99 | 6 |

Lielākais minējumu skaits testos bija 6.

## Papildu funkcija
Programma pārbauda pretrunīgas atbildes. Ja spēlētājs sniedz neiespējamas atbildes, dators paziņo par krāpšanos un pārtrauc spēli.