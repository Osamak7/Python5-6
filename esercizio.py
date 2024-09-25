import json , sys

# Funzione per serializzare i dati in un file JSON
def SerializzaJson(dati, percorso_file):
    try:
        with open(percorso_file, 'w') as json_file:
            json.dump(dati, json_file)  # Serializza il dizionario in JSON e lo scrive nel file
        return True
    except Exception as e:
        print(f"Errore durante la serializzazione: {e}")
        return False

# Funzione per deserializzare i dati da un file JSON
def DeserializzaJson(percorso_file):
    try:
        with open(percorso_file, 'r') as json_file:
            dati = json.load(json_file)  # Legge i dati JSON dal file e li converte in un dizionario
        return dati
    except Exception as e:
        print(f"Errore durante la deserializzazione: {e}")
        return None

# Esempio di utilizzo
mio_dizionario = {
    "marca": "Ford",
    "elettrico": False,
    "anno": 1964,
    "colori": ["rosso", "bianco", "blu"]
}

percorso_file = "dati_auto.json"

# Serializza il dizionario in un file JSON
successo = SerializzaJson(mio_dizionario, percorso_file)
print("Serializzazione avvenuta con successo:", successo)

# Deserializza il file JSON in un dizionario
dati_deserializzati = DeserializzaJson(percorso_file)
print("Dati deserializzati:", dati_deserializzati)
