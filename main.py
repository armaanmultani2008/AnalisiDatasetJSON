# ANALISI DATASET JSON
# Catalogo giochi PS4 e PS5
# Fonte: https://www.kaggle.com/datasets/evgeny1928/playstation-games-info

import json
import matplotlib.pyplot as plt

# --------------------------------------------------
# CARICAMENTO FILE JSON
# --------------------------------------------------

with open("data/output.json", "r", encoding="utf-8") as file: # "r" = read
    dati = json.load(file)

giochi = list(dati.values())


# --------------------------------------------------
# CLASSIFICA 20 GIOCHI CON RATING PIÙ ALTO (min 10.000 voti)
# --------------------------------------------------

giochi_filtrati = []

for gioco in giochi:
    rating = gioco.get("rating")
    voti = gioco.get("votes")

    if isinstance(rating, (int, float)) and isinstance(voti, int) and voti >= 10000:
        giochi_filtrati.append(gioco)

giochi_ordinati_rating = sorted(
    giochi_filtrati,
    key=lambda gioco: gioco["rating"],
    reverse=True
)

print("\nTop 20 giochi per rating (min 10.000 voti):\n")

for i, gioco in enumerate(giochi_ordinati_rating[:20], start=1):
    print(f"{i}. {gioco['title']} - Rating: {gioco['rating']} - Voti: {gioco['votes']}")


# --------------------------------------------------
# CLASSIFICA 20 GIOCHI PIÙ VOTATI
# --------------------------------------------------

giochi_ordinati_voti = sorted(
    [g for g in giochi if isinstance(g.get("votes"), int)],
    key=lambda gioco: gioco["votes"],
    reverse=True
)

print("\nTop 20 giochi più votati:\n")

for i, gioco in enumerate(giochi_ordinati_voti[:20], start=1):
    print(f"{i}. {gioco['title']} - Voti: {gioco['votes']}")


# --------------------------------------------------
# NUMERO DI GIOCHI PER ANNO
# --------------------------------------------------

conteggio_per_anno = {}

for gioco in giochi:
    data = gioco.get("release_date")
    if isinstance(data, str) and "/" in data:
        try:
            anno = int(data.split("/")[-1]) #può lanciare un'eccezione durante il parsing in int()
            conteggio_per_anno[anno] = conteggio_per_anno.get(anno, 0) + 1
        except ValueError: #cattura l'eccezione
            pass #ignora e continua

print("\nNumero di giochi per anno:\n")

for anno in sorted(conteggio_per_anno):
    print(f"{anno}: {conteggio_per_anno[anno]}")


# --------------------------------------------------
# GIOCHI PER GENERE
# --------------------------------------------------

giochi_per_genere = {}

for gioco in giochi:
    generi = gioco.get("genres")
    if isinstance(generi, list):
        for genere in generi:
            giochi_per_genere[genere] = giochi_per_genere.get(genere, 0) + 1


# --------------------------------------------------
# GIOCHI PER PIATTAFORMA
# --------------------------------------------------

giochi_per_piattaforma = {}

for gioco in giochi:
    piattaforme = gioco.get("platforms")
    if isinstance(piattaforme, list):
        for piattaforma in piattaforme:
            giochi_per_piattaforma[piattaforma] = giochi_per_piattaforma.get(piattaforma, 0) + 1


# --------------------------------------------------
# RATING MEDIO PER RANGE DI PREZZO
# --------------------------------------------------

# Si defniscono i range di prezzo
range_prezzi = [(0, 0), (1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 100)]
etichette = ["0", "1-10", "11-20", "21-30", "31-40", "41-50", "51-100"]

# Si creano dizionari per somma dei rating e conteggio per ogni range
somma_rating_range = {i: 0 for i in range(len(range_prezzi))}
conteggio_range = {i: 0 for i in range(len(range_prezzi))}

# Si assegna ogni gioco al suo range
for gioco in giochi:
    prezzo = gioco.get("price")
    rating_val = gioco.get("rating")
    
    if isinstance(prezzo, (int, float)) and isinstance(rating_val, (int, float)):
        for i, (min_p, max_p) in enumerate(range_prezzi):
            if min_p <= prezzo <= max_p:
                somma_rating_range[i] += rating_val
                conteggio_range[i] += 1
                break

# Si calcola rating medio per ogni range
rating_medio_range = [
    (somma_rating_range[i] / conteggio_range[i]) if conteggio_range[i] > 0 else 0
    for i in range(len(range_prezzi))
]

# Grafico a barre
plt.figure()
plt.bar(etichette, rating_medio_range, color="skyblue")
plt.xlabel("Range di prezzo (€)")
plt.ylabel("Rating medio")
plt.title("Rating medio dei giochi per range di prezzo")
plt.show()


# --------------------------------------------------
# GRAFICO LINE: RATING MEDIO PER ANNO
# --------------------------------------------------

somma_rating_anno = {}
conteggio_rating_anno = {}

for gioco in giochi:
    data = gioco.get("release_date")
    rating_val = gioco.get("rating")

    if isinstance(data, str) and "/" in data and isinstance(rating_val, (int, float)):
        try:
            anno = int(data.split("/")[-1])
            somma_rating_anno[anno] = somma_rating_anno.get(anno, 0) + rating_val
            conteggio_rating_anno[anno] = conteggio_rating_anno.get(anno, 0) + 1
        except ValueError:
            pass

anni = sorted(somma_rating_anno)
rating_medio = [
    somma_rating_anno[a] / conteggio_rating_anno[a]
    for a in anni
]

plt.figure()
plt.plot(anni, rating_medio)
plt.xlabel("Anno")
plt.ylabel("Rating medio")
plt.title("Evoluzione del rating medio nel tempo")
plt.show()


# --------------------------------------------------
# GRAFICO BAR: RATING MEDIO PER GENERE
# --------------------------------------------------

somma_rating_genere = {}
conteggio_genere = {}

for gioco in giochi:
    rating_val = gioco.get("rating")
    generi = gioco.get("genres")

    if isinstance(rating_val, (int, float)) and isinstance(generi, list):
        for genere in generi:
            somma_rating_genere[genere] = somma_rating_genere.get(genere, 0) + rating_val
            conteggio_genere[genere] = conteggio_genere.get(genere, 0) + 1

generi = list(somma_rating_genere.keys())
rating_medio_genere = [
    somma_rating_genere[g] / conteggio_genere[g]
    for g in generi
]

plt.figure()
plt.bar(generi, rating_medio_genere)
plt.xticks(rotation=45, ha="right")
plt.title("Rating medio per genere")
plt.show()
