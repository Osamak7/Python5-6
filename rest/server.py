from flask import Flask, json, request
from myJson import JsonSerialize, JsonDeserialize

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)


@api.route("/add_cittadino", methods=["POST"])
def GestisciAddCittadino():
    #prendi i dati della richiesta
    content_type = request.headers.get("Content-Type")
    print("Ricevuta chiamata" + content_type)
    if content_type == "application/json":
        JRequest = request.json
        sCodiceFiscale = JRequest["codiceFiscale"]
        print("Ricevuto" + sCodiceFiscale)

        #carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = JRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            JResponse = {"Error":"000", "Msg" : "Ok"}
            return json.dumps(JResponse), 200
        else:
            JResponse = {"Error":"001", "Msg" : "Codice fiscale gia presente in anagrafe"}
            return json.dumps(JResponse), 200
    else:
        return "Errore, formato non riconosciuto", 401
        #controlla che il cittadino non è gia presente in anagrafe
        #rispondi


api.run(host="127.0.0.1",port= 8080)