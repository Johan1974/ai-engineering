# AI Engineering Roadmap 2026

Persoonlijk leerplan en voortgangslog voor mijn traject naar AI Engineer.

---

## Huidige Focus
- [x] DataCamp `dictionaries-pandas` ex11 afgerond in `exercises/DataCamp/dictionary_naar_dataframe_2.py`
- [x] DataCamp `dictionaries-pandas` ex12 afgerond in `exercises/DataCamp/csv_to_dataframe_1.py`
- [x] DataCamp `dictionaries-pandas` ex13 afgerond in `exercises/DataCamp/csv_to_dataframe_2.py`
- [x] Kolommen selecteren met `[]` — `exercises/DataCamp/square_brackets_1.py` (oefening vóór rij-slices; geen ex-nummer in bestand)
- [x] DataCamp `dictionaries-pandas` [ex16](https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=16) — `exercises/DataCamp/square_brackets_2.py`
- [x] DataCamp `dictionaries-pandas` [ex17](https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=17) — `exercises/DataCamp/loc_and_iloc_1.py`
- [x] DataCamp `dictionaries-pandas` [ex18](https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=18) — `exercises/DataCamp/loc_and_iloc_2.py`
- [ ] **Volgende stap:** in DataCamp de oefening na [ex18](https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=18) openen en hier een nieuw `snake_case.py` in `exercises/DataCamp/` voor aanmaken

---

## DataCamp Checklist (Interactive)

### Intermediate Python - Dictionaries & Pandas
- [x] ex11 - dictionary naar DataFrame
- [x] ex12 - CSV inlezen met pandas
- [x] ex13 - CSV inlezen met `index_col`
- [x] ex14–ex15 (samengevat) - DataFrame selecties met `[]` — `square_brackets_1.py`
- [x] ex16 - rijen slicen met `[]` — `square_brackets_2.py`
- [x] ex17 - `loc` en `iloc` — `loc_and_iloc_1.py`
- [x] ex18 - `loc` met rijen én kolommen — `loc_and_iloc_2.py`

### Professional Code (na Intermediate Python)
- [ ] Start Python Programming Track (OOP)
- [ ] Oefeningen met functions/classes in aparte `.py` bestanden
- [ ] Eerste refactor: script opsplitsen in herbruikbare functies

### Data Manipulation met pandas
- [ ] Intro tot selecteren en filteren
- [ ] Groeperen en aggregeren
- [ ] Werken met missende waarden

---

## Workflow Afspraken
- [x] Bestandsnamen altijd in `snake_case`
- [x] Elke opdracht krijgt een eigen `.py` bestand in `exercises/DataCamp/`
- [x] Na elke afgeronde opdracht: herinnering voor Git commit
- [x] **Na elke “afgerond”-melding door jou:** de assistent voert een **korte verificatie** uit (`cd exercises/DataCamp` + script met project-`.venv` draaien), vat de output samen (geen volledige dump tenzij nodig), en werkt **Huidige Focus** + **checklist** + **logboek** in dit bestand bij — tenzij jij expliciet alleen commentaar zonder test vraagt.
- [x] **DataCamp-URL na goedkeuring:** zodra DataCamp de oefening als correct heeft beoordeeld, zet jij de volledige campus-URL **bovenaan** in het bijbehorende `.py`-bestand (regel 1, als commentaar, zoals bij ex16/ex17). In de chat mag je diezelfde URL plakken wanneer je meldt dat iets af is — dan kan de assistent oefeningnummer en roadmap exact koppelen.

Commit-formaat:
```bash
git add .
git commit -m "complete datacamp exNN: korte beschrijving"
```

### No-Spoiler Modus (strikte leerregel)
- [x] Bij nieuwe opdrachten geeft de assistent nooit direct de volledige code-oplossing.
- [x] Geen ghost-text/autocomplete die de puzzeloplossing verklapt.
- [x] Alleen hints geven als ik er expliciet om vraag.
- [x] Ik typ de code altijd zelf, ook als er fouten in zitten.
- [x] Correcties of uitleg pas nadat ik de code heb uitgevoerd en een error deel.

### Deep Dive Check (verplicht per afgerond DataCamp-hoofdstuk)
- [x] Geen nieuw hoofdstuk zonder Deep Dive Check.
- [x] De assistent stelt exact 3 vragen per hoofdstuk met deze mix:
  - **Syntax:** "Hoe schrijf je dit korter?"
  - **Concept:** "Wat gebeurt er onder de motorkap als we `index_col=0` gebruiken?"
  - **Scenario:** "Stel dat de CSV geen komma's maar puntkomma's gebruikt, wat pas je aan?"
- [x] Scoring op basis van je antwoorden:
  - **Groen:** "Kennis is solide, ga door naar de volgende DataCamp module."
  - **Oranje:** "Je snapt de truc, maar bekijk [onderwerp] nog een keer in `notes/`."
  - **Rood:** "Stop. We gaan eerst een eigen oefening doen in `projects/` voordat je verder gaat met nieuwe stof."

### Review & Challenge (verplicht bij `@bestandsnaam`)
- [x] Bij elk verzoek met `@bestandsnaam` start automatisch deze cyclus:
  - **Code Review:** verbeterpunten voor leesbaarheid en Pythonic standards
  - **Kennis-Check:** exact 2 scherpe logica-vragen
  - **Strategisch Advies:** "Stof beheerst, ga door met DataCamp." of "Nog niet stabiel, doe eerst een extra lokale oefening."
  - **Update-voorstel:** altijd voorstellen om deze roadmap direct te updaten

---

## Strategische Evaluatie
Na elke **3 afgeronde oefeningen** voert de assistent een korte analyse uit op basis van code in `exercises/DataCamp/`.

### Evaluatieformat (verplicht)
- **DataCamp vs. Praktijk:** beheers ik de concepten echt, of is een mini-project nodig?
- **Relevantie voor AI Engineering:** blijft DataCamp nu de beste route, of verschuiven naar `scikit-learn`, `PyTorch`, `numpy`, `fastapi`?
- **Beslissingsmoment (expliciet):**
  - `GA DOOR met Intermediate Python`
  - `STOP en focus op [onderwerp X]`

### Ritme en trigger
- [x] Evaluatie 1 na ex11-ex13 (afgerond)
- [x] Evaluatie 2 na ex14-ex17 (afgerond — zie logboek)
- [ ] Evaluatie 3 na de volgende 3 oefeningen

### Strategische evaluatie - huidig besluit
- **DataCamp vs. Praktijk:** basisconcepten zitten goed; na nog een paar pandas-oefeningen een mini-project toevoegen voor transfer naar praktijk.
- **Relevantie:** pandas/python-fundamenten zijn nu nog relevant voor AI Engineering.
- **Beslissingsmoment:** `GA DOOR met Intermediate Python`

---

## Snelstart Commando's
Voer uit vanuit de projectroot:

```bash
cd /root/dev/ai-engineering/exercises/DataCamp
../../.venv/bin/python dictionary_naar_dataframe_2.py
../../.venv/bin/python csv_to_dataframe_1.py
../../.venv/bin/python csv_to_dataframe_2.py
../../.venv/bin/python square_brackets_1.py
../../.venv/bin/python square_brackets_2.py
../../.venv/bin/python loc_and_iloc_1.py
../../.venv/bin/python loc_and_iloc_2.py
```
*(Scripts verwachten `csv/cars.csv` relatief t.o.v. `exercises/DataCamp/`.)*

---

## Coach-protocol voor nieuwe sessies
Als ik vraag: **"Wat is de volgende stap?"**, dan moet de assistent:
- [ ] eerst `exercises/DataCamp/` scannen
- [ ] deze roadmap/checklist als bron gebruiken
- [ ] exact 1 volgende DataCamp-opdracht voorstellen
- [ ] exact 1 nieuw `.py` bestand voorstellen in `snake_case`
- [ ] afsluiten met een reminder om te committen na afronden

---

## Logboek & Voortgang
- [2026-04-29] CSV import met `index_col=0` afgerond.
- [2026-04-29] `square_brackets_1.py`, `square_brackets_2.py` (ex16), `loc_and_iloc_1.py` (ex17) afgerond; scripts gedraaid vanuit `exercises/DataCamp/` — exit code 0, `loc`/`iloc`-output matcht (JPN/AUS/EG).
- [2026-04-29] **Evaluatie 2 (kort):** selecteren met `[]`, rij-slices en `loc`/`iloc` sluit aan op roadmap-doel; `GA DOOR met Intermediate Python`. Optioneel: Deep Dive Check op `loc` vs `iloc` bij volgende sessie als je dat wilt.
- [2026-04-29] [ex18](https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=18) — `loc_and_iloc_2.py`; script gedraaid — exit code 0 (MOR/`drives_right`, subframe RU+MOR). Richting **Evaluatie 3:** nog 2 oefeningen na ex18 tot de volgende blok-evaluatie.