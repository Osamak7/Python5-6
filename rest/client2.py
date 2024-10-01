import json, requests

base_url = "http://127.0.0.1:8080"



def RichiediDatiCittadino():
    nome = input("\ninserisci il nome: \n")
    cognome = input("\ninserisci il cognome: \n")
    dataNascita = input("\ninserisci la data di nascita: \n")
    codFiscale = input("\ninserisci il codice fiscale: \n")
    jRequest = {"nome" : nome, "cognome" : cognome, "data di nascita" : dataNascita, "codice fiscale" : codFiscale}
    return jRequest

def Gestisci_Dati():
    jRequest = input("inserisci il codice fiscale del cittadino per vedere i suoi dati\n")
    return jRequest

def modifica_cit():
    print("\nse non vuoi modificare scrivi \"salta\"\n")
    codFiscale = input("inserisci il codice fiscale del cittadino che vuoi modificare i dati\n")
    nome = input("\ninserisci il nuovo nome: \n")
    cognome = input("\ninserisci il nuovo cognome: \n")
    dataNascita = input("\ninserisci la nuova data di nascita: \n")
    jRequest = {"nome" : nome, "cognome" : cognome, "data di nascita" : dataNascita, "codice fiscale" : codFiscale}
    return jRequest 

def elimina_cit():
    jRequest = input("inserisci il codice fiscale del cittadino che vuoi eliminare\n")
    return jRequest


def CreaInterfaccia():
    print("\nOperazioni disponibili:\n")
    print("1. Inserisci cittadino (es: atto di nascita)\n")
    print("2. Richiedi dati del cittadini (es: cert. residenza\n")
    print("3. Modifica dati del cittadino\n")
    print("4. Elimina dati del cittadino\n")
    print("5. Exit\n")

CreaInterfaccia()

SOper = (input("seleziona operazione\n"))

while (SOper != "5"):
    
    if SOper =="1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest =  RichiediDatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("attenzione problemi")

    elif SOper == "2":
        api_url = base_url + "/read_cittadino"
        codiceFiscaleCittadino = input("inserisci il tuo codice fiscale")
        api_url+= "/" +codiceFiscaleCittadino
        try:
            response = requests.get(api_url)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("attenzione problemi")

    elif SOper == "3":
        api_url = base_url + "/modifica_cittadino"
        jsonDataRequest = modifica_cit()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("attenzione problemi")

    elif SOper == "4":
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = elimina_cit()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("attenzione problemi")

    CreaInterfaccia()
    SOper = input("\nSeleziona operazione\n")