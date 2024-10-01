from flask import Flask,json,request
from myJson import JsonDeserialize, JsonSerialize

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route("/add_cittadino", methods= ["POST"])
def GestisciAddCittadino():
    #prendi dati della richiesta
    content_type = request.headers.get('Content_Type')
    print("\n Ricevuta chiamata" + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("codice fiscale ricevuto: " + sCodiceFiscale)

        #carico l anagrafe
        dAnagrafe = deserializza_json(sFileAnagrafe)

           #controlla se non ce sta
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            serializza_json(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error" : "000", "Msg" : "ok"}
            return json.dumps(jResponse),200
        
        else:

            jResponse = {"Error" : "001", "Msg" : "CODICE FISCALE GIÀ PRESENTE"}
            return json.dumps(jResponse),200
    
    else:
        return "Errore, Formato non riconosciuto",401
 
@api.route("/gestisci_dati", methods= ["POST"])
def GestisciDati():

    #prendo dati della richiesta
    content_type = request.headers.get('Content_Type')
    print("\n Ricevuta chiamata" + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest
        print("codice fiscale ricevuto: " + sCodiceFiscale)

    dAnagrafe = deserializza_json(sFileAnagrafe)

           #controlla se non ce sta
    if sCodiceFiscale in dAnagrafe:

        #risposta
        jResponse = {"Error" : "000", "Msg" : f"DATI UTENTE RICHIESTI {dAnagrafe[sCodiceFiscale]}"}

        return json.dumps(jResponse),200
    else:

        jResponse = {"Error" : "003", "Msg" : "CODICE FISCALE SBAGLIATO"}
        return json.dumps(jResponse),200


@api.route("/modifica_cittadino", methods= ["POST"])
def GestisciModifica():
    #prendi dati della richiesta
    content_type = request.headers.get('Content_Type')
    print("\n Ricevuta chiamata" + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("codice fiscale ricevuto: " + sCodiceFiscale)

        #carico l anagrafe
        dAnagrafe = deserializza_json(sFileAnagrafe)

           #controlla se non ce sta
        if sCodiceFiscale in dAnagrafe:
            for k,v in jRequest.items():
                if v != "salta":
                    dAnagrafe[sCodiceFiscale][k] = v



            serializza_json(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error" : "000", "Msg" : "ok"}
            return json.dumps(jResponse),200
        
        else:

            jResponse = {"Error" : "001", "Msg" : "ERRORE DURANTE LA MODIFICA"}
            return json.dumps(jResponse),200
        

"/elimina_cittadino"
@api.route("/elimina_cittadino", methods= ["POST"])
def GestisciEliminazione():
    #prendi dati della richiesta
    content_type = request.headers.get('Content_Type')
    print("\n Ricevuta chiamata" + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest

        #carico l anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)

           #controlla se non ce sta e esegue l operazione
        if sCodiceFiscale in dAnagrafe:
            del dAnagrafe[sCodiceFiscale]
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error" : "000", "Msg" : "ok"}
            return json.dumps(jResponse),200
        else:

            jResponse = {"Error" : "001", "Msg" : "ERRORE DURANTE LA MODIFICA"}
            return json.dumps(jResponse),200
        
        



api.run(host= "127.0.0.1", port="8080")