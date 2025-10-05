# Reseptit

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan reseptejä.
* Käyttäjä näkee sovellukseen lisätyt reseptit. Käyttäjä näkee sekä itse lisäämänsä    että muiden käyttäjien lisäämät reseptit.
* Käyttäjä pystyy etsimään reseptejä hakusanalla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä reseptejä.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät reseptit.
* Käyttäjä pystyy valitsemaan reseptille yhden tai useamman luokittelun (esim. alkuruoka, jälkiruoka, vegaani).
* Käyttäjä pystyy lisäämään kommentteja omiin ja muiden käyttäjien resepteihin.
* Käyttäjä pystyy lisäämään kuvia omiin resepteihin.

## Sovelluksen asentaminen

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```







