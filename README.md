# SpotifyStats

SpotifyStats is a simple Python script that uses the Spotify data export to generate some statistics about your listening habits.

## Usage

1. Download your Spotify data from [here](https://www.spotify.com/us/account/privacy/).
2. Extract the archive and place the folder MyData in ./data/

* If you have multiple data archives, you can place them in the same folder with numbers appended to the folder name, e.g. MyData1, MyData2, etc.
* If you want to specify a date range you can set the `start_date` and `end_date` variables in `main.py` to the desired dates.

Note: The Spotify wrapper use a date range from January 1st to October 31st, 2017.

Exemple of stats:
```
Donnée du 2020-09-25 au 2021-09-26
Pour l'année 2020 tu as écouté 42992.64 minutes ou 716.54 heures
Pour l'année 2021 tu as écouté 85215.15 minutes ou 1420.25 heures
Au total tu as écouté 128207.8 minutes ou 2136.8 heures

Liste des artists que tu as écouté le plus:

#1: bbno$ pour un total de 4038 fois
#2: Spillage Village pour un total de 2328 fois
#3: Mac Miller pour un total de 1728 fois
#4: easy life pour un total de 1432 fois
#5: EARTHGANG pour un total de 1376 fois
#6: FouKi pour un total de 1250 fois
#7: Isaiah Rashad pour un total de 1047 fois
#8: Geoffroy pour un total de 837 fois
#9: Glass Animals pour un total de 782 fois
#10: Hippie Sabotage pour un total de 776 fois

Liste des artists que tu as écouté le plus:
#1: Baptize (with JID & EARTHGANG feat. Ant Clemons) pour un total de 580 fois
#2: Gone pour un total de 568 fois
#3: Mecca (with JID & EARTHGANG) pour un total de 547 fois
#4: 10 Bands pour un total de 504 fois
#5: Money Trees pour un total de 443 fois
#6: Voodoo pour un total de 442 fois
#7: nursery pour un total de 437 fois
#8: thankful pour un total de 405 fois
#9: shining on my ex pour un total de 398 fois
#10: Goodie Bag pour un total de 373 fois
```

