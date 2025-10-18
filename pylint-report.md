# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:76:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:114:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:150:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:163:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:188:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:205:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:242:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:256:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:242:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:263:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:267:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:284:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:293:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:284:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:303:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module items
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:54:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:27:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

------------------------------------------------------------------
Your code has been rated at 8.35/10 (previous run: 8.29/10, +0.06)
```

Käydään seuraavaksi läpi tarkemmin raportin sisältö ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Raportin suurin osa ilmoituksista koostuu seuraavan tyyppisistä ilmoituksista:

```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Ilmoituksissa kerrotaan, että moduuleista tai funktioista puuttuvat docstring-kommentit. Tämä on tietoinen ratkaisu. Projektissa on päätetty, ettei siinä käytetä docstring-kommentteja.

## Tarpeeton else-haara

Raportissa on seuraavat ilmoitukset liittyen `else`-haaroihin:

```
app.py:256:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:293:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:27:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```

Esimerkki koodista, jota ilmoitus koskee:

```python
if "remove" in request.form:
    items.remove_item(item_id)
    return redirect("/")
else:
    return redirect("/item/" + str(item_id))
```

Sama koodi voitaisiin myös kirjoittaa tiiviimmin:

```python
if "remove" in request.form:
    items.remove_item(item_id)
    return redirect("/")
return redirect("/item/" + str(item_id))
```

Sovelluksen kehittäjän näkemyksen mukaan `else`-haara kuitenkin tekee ohjelmointilogiikasta selkeämmän ja korostaa vaihtoehtoisia toimintapolkuja.

## Puuttuva palautusarvo

Raportissa on seuraavat ilmoitukset liittyen funktion palautusarvoon:

```
app.py:242:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:284:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
Ilmoitukset varoittavat tilanteista, joissa funktio ei teoriassa palauta arvoa kaikissa tapauksissa. Esimerkiksi seuraava funktio, joka käsittelee vain GET- ja POST-metodit, saa tästä huomautuksen.

```python
@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    require_login()

    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))
```

Koska funktion dekoroinnissa on rajattu sallitut metodit, käytännössä tällaista tilannetta ei voi syntyä.

## Vakion nimi

Raportissa on seuraava ilmoitus liittyen vakion nimeen:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Tässä muuttujan nimen tulisi periaatteessa olla kirjoitettu `SECRET_KEY`, koska se tulkitaan vakioksi. Tässä projektissa nimi on kuitenkin kirjoitettu pienillä kirjaimilla, koska se sopii paremmin tapaan, jolla muuttujaa käytetään koodissa:

```python
app.secret_key = config.secret_key
```

## Vaarallinen oletusarvo

Raportissa on seuraavat ilmoitukset liittyen vaaralliseen oletusarvoon:

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Esimerkki koodista, jota ilmoitus koskee:

```python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```
Ilmoitukset liittyvät funktioihin, joissa tyhjä lista on parametrin oletusarvona. Yleisesti tämä voi olla riskialtista, jos listaa muokataan funktion sisällä. Tässä tapauksessa listaa ei kuitenkaan muuteta.
