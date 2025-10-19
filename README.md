# Reseptit

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan reseptejä.
* Käyttäjä näkee sovellukseen lisätyt reseptit. Käyttäjä näkee sekä itse lisäämänsä, että muiden käyttäjien lisäämät reseptit.
* Käyttäjä pystyy etsimään reseptejä hakusanalla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä reseptejä.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät reseptit.
* Käyttäjä pystyy valitsemaan reseptille luokittelun (esim. alkuruoka, jälkiruoka, vegaani).
* Käyttäjä pystyy lisäämään kommentteja omiin ja muiden käyttäjien resepteihin.
* Käyttäjä pystyy lisäämään kuvan omaan reseptiin.


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

## Raportti suuren tietomäärän käsittelystä

**Testidata (seed.py):**
- users = 1000
- items = 10^6
- comments = 10^7
- Jokaiselle kommentille arvottu (user_id, item_id)

**Ajanmittaus:**
- Lisätty `@before_request` ja `@after_request` tulostamaan `elapsed time: … s`.

**Esimerkkirivejä lokista:**
```
elapsed time: 0.05 s
127.0.0.1 - - [19/Oct/2025 21:46:39] "GET / HTTP/1.1" 200 -
elapsed time: 0.01 s
127.0.0.1 - - [19/Oct/2025 21:46:39] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [19/Oct/2025 21:46:44] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:46:44] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [19/Oct/2025 21:46:46] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:46:46] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [19/Oct/2025 21:46:49] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.01 s
127.0.0.1 - - [19/Oct/2025 21:46:49] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [19/Oct/2025 21:46:52] "GET /5 HTTP/1.1" 200 -
```
**Tulokset:**

- Sivutus rajoittaa haettujen rivien määrän.
- Indeksi `idx_comments_item` tekee kommenttien liittämisestä tehokasta. 
- Vaikka datamäärä kasvatettiin suureksi, sivujen vasteaika pysyi ~0.00–0.05 s.




