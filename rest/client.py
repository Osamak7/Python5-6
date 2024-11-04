import json, requests

base_url = 'https://127.0.0.1:8080'

def Data():

    anno: str = input('Inserisci l\'anno di nascita del cittadino: ')
    con = True

    while con:

        try:
            if len(anno) == 4:
                _ = int(anno)
                con = False
            else:
                anno: str = input('Inserisci l\'anno di nascita del cittadino: ')
        except:

            anno: str = input('Inserisci l\'anno di nascita del cittadino: ')
            
    mese: str = input('Inserisci il mese di nascita del cittadino: ')
    con = True

    while con:

        try:
            if len(mese) == 2:
                test = int(mese)
                con = False
            elif len(mese) == 1:
                test = int(mese)
                con = False
                mese = f"0{mese}"
            else:
                mese: str = input('Inserisci il mese di nascita del cittadino: ')

            if (test > 12) or (test < 1):

                con = True
                mese: str = input('Inserisci il mese di nascita del cittadino: ')
        except:

            mese: str = input('Inserisci il mese di nascita del cittadino: ')


    giorno: str = input('Inserisci il giorno di nascita del cittadino: ')
    con = True

    while con:

        try:
            if len(giorno) == 2:
                test = int(giorno)
                con = False
            elif len(giorno) == 1:
                test = int(giorno)
                con = False
                giorno = f"0{giorno}"
            else:
                giorno: str = input('Inserisci il giorno di nascita del cittadino: ')

            if (test > 31) or (test < 1):

                con = True
                giorno: str = input('Inserisci il giorno di nascita del cittadino: ')
        except:

            giorno: str = input('Inserisci il giorno di nascita del cittadino: ')        

    data = f"{anno}-{mese}-{giorno}"

    return data

def RIchiediDatiCittadino(user, password):

    nome: str = input('Inserisci il nome del cittadino: ')
    cognome: str = input('Inserisci il cognome del cittadino: ')
    cf: str = input('Inserisci il codice fiscale del cittadino: ')

    data = Data()

    
    jRequest = {"cittadino":{'nome':nome, 'cognome':cognome, 'dataNascita':data,'codiceFiscale': cf}, "operatore":{'user': user, 'password': password}}
    return jRequest

def InvioCodiceFiscale(user, password):
    
    codiceFiscale: str = input('Inserisci il codice fiscale del cittadino: ')

    jRequest = {"cittadino":{'codiceFiscale': codiceFiscale}, "operatore":{'user': user, 'password': password}}
    return jRequest

def ModificaDatiCittadino(user, password):
    
    codiceFiscale: str = input('Inserisci il codice fiscale del cittadino: ')

    ris = input('Vuoi cambiare il codice fiscale:(s/n) ')
    if ris == 's':

        cf = input('Inserire il nuovo codice fiscale: ')
    else:

        cf = 0

    ris = input('Vuoi cambiare il nome:(s/n) ')
    if ris == 's':

        nome = input('Inserire il nuovo nome: ')
    else:

        nome = 0

    ris = input('Vuoi cambiare il cognome:(s/n) ')
    if ris == 's':

        cognome = input('Inserire il nuovo cognome: ')
    else:

        cognome = 0

    ris = input('Vuoi cambiare la data di nascita:(s/n) ')
    if ris == 's':

        data = Data()
    else:

        data = 0

    jRequest = {'codiceFiscale': codiceFiscale, 'modifiche':{'codiceFiscale':cf, 'nome':nome, 'cognome':cognome, 'dataNascita':data}, "operatore":{'user': user, 'password': password}}
    return jRequest

def EliminaDatiCittadino(user, password):
    
    codiceFiscale: str = input('Inserisci il codice fiscale del cittadino: ')

    jRequest = {"cittadino":{'codiceFiscale': codiceFiscale}, "operatore":{'user': user, 'password': password}}
    return jRequest

def CreaInterfaccia(permesso):

    print()
    print('Quali operazioni vuoi eseguire: 1=Lettura ')
    a= input("inserisci 1 se vuoi ")
    if(permesso == 'w'):
        print()
        print('1. Inserisci cittadino (es. atto di nascita)')
        print('2. Richiedi dati cittadino (es. cert. residenza)')
        print('3. Modifica dati cittadino')
        print('4. Elimina cittadino')
        print('5. Exit')
    
    elif(permesso == 'r'):
        
        print()
        print('2. Richiedi dati cittadino (es. cert. residenza)')
        print('5. Exit')

    else:
        
        print()
        print('5. Exit')

def accedi():
    
    print()
    user: str = input('Inserisci l\'email di login: ')
    print()
    password: str = input('Inserisci password: ')

    jRequest = {"operatore":{'user': user, 'password': password}}
    return jRequest


login = False

while login == False:

    api_url = base_url + '/accedi'
    jsonDataRequest = accedi()

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
        print(data1)
    except:
        print('Problemi di connessione con il server, riprova più tardi')

    if data1['msg'] == 'ok':

        login = True
        user: str = jsonDataRequest["operatore"]['user']
        password: str = data1['user'][1]
        permesso: str = data1['user'][2]
        note: str = data1['user'][3]

if login:
    CreaInterfaccia(permesso)
    print()
    sOper = input('Selezione operazione: ')

    while (sOper != '5'):    

        if sOper == '1':
            
            if permesso == 'w':

                api_url = base_url + '/add_cittadino'
                jsonDataRequest = RIchiediDatiCittadino(user, password)

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    data1 = response.json()
                    print(data1)
                except:
                    print('Problemi di connessione con il server, riprova più tardi')
            else:

                print('Permesso negato')
        elif sOper == '2':

            if(permesso == 'r')or(permesso == 'w'):

                api_url = base_url + '/info_cittadino'
                jsonDataRequest = InvioCodiceFiscale(user, password)
            
                res = True

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    
                    data1 = response.json()

                    res = False
                
                    info = data1.pop('info')
                    codfis = info[0]
                    nome = info[1]
                    cognome = info[2]
                    data = info[3]
                    

                    print(data1)
                    print()
                    print(f'NOME: {nome}')
                    print(f'COGNOME: {cognome}')
                    print(f'DATA DI NASCITA: {data}')
                    print(f'CODICE FISCALE: {codfis}')


                except:

                    if res:
                        print('Problemi di connessione con il server, riprova più tardi')
                    else:
                        print(data1)
            else:

                print('Permesso Negato')
        elif sOper == '3':
            

            if permesso == 'w':

                api_url = base_url + '/modifica_cittadino'
                jsonDataRequest = ModificaDatiCittadino(user, password)

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    
                    data1 = response.json()
                    
                    print(data1)
                    print()


                except:
                    print('Problemi di connessione con il server, riprova più tardi')

            else:

                print('Permesso Negato')

        elif sOper == '4':
            
            if permesso == 'w':
                
                api_url = base_url + '/elimina_cittadino'
                jsonDataRequest = EliminaDatiCittadino(user, password)

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    
                    data1 = response.json()
                    
                    print(data1)
                    print()


                except:
                    print('Problemi di connessione con il server, riprova più tardi')
            
            else:

                print('Permesso Negato')

        else:
            
            print('Operazione inesistente')
        
        CreaInterfaccia(permesso)
        print()
        sOper = input('Selezione operazione: ')