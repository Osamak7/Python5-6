import requests, json, sys
#requests: facilita l'invio di richieste HTTP per
#       comunicare con server o API.

#json: gestisce i dati in formato JSON,
#       spesso usato per inviare e ricevere dati da API.

#sys: permette di accedere a funzioni di sistema,
#       come l’input/output standard, utile per la 
#       gestione degli errori o per terminare il programma
#       in caso di problemi.
import urllib3 #serve per gestire le richieste http 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#disabilito i gli errori che mi darebbe se mi collego 
# a un https seza una vera conferma 


base_url = "https://127.0.0.1:8080"# Questa è l'URL di base del server a cui il programma si connetterà.
                                    #In questo caso, indica un server locale su HTTPS.

def GetDatiCittadino(): # setto i dati del cittadino
    nome = input("inserisci il nome: ")
    cognome = input("inserisci il cognome: ")
    dataNa = input("inserisci la data di nascita: ")
    cf = input("inserisci il codice fiscale: ")
    daticittadino = {
        "nome": nome,
        "cognome" : cognome,
        "dataNascita" : dataNa,
        "codFiscale" : cf
    }
    return daticittadino

def GetCodiceFiscale():
    cf = input("inserisci codice fiscale: ")
    return {"codFiscale": cf}

def EseguiOperazione():
    pass

def EffettuaPrimoLogin():
    global sUsername, sPassword, sPrivilegio, iPrimoLoginEffettuato

    sUsername = input("Inserisci username: ")
    sPassword= input("inserisci password: ")
    #compongo la richiesta 
    jsonRequest ={
        "username" : sUsername,
        "password" : sPassword
    }
    try:
        #mando i dati al server
        api_url = base_url + "/login"
        response= requests.post(api_url, 
                                json= jsonRequest,
                                  verify=False)# verify=False indica di ignorare la verifica del certificato SSL 
                                            #(utile per server locali o di sviluppo, ma rischioso in produzione)

        #processa la risposta del server
        if response.status_code == 200:
            