from flask import Flask, render_template, request, redirect, url_for

api = Flask(__name__)

# Dizionario per memorizzare gli utenti (in memoria)
utenti: dict[str, str] = {
    "mario@777.it": "rossi",
    "gianni@12.it": "derossi",
    "anita@123.com": "garibaldi"
}

# Route principale, ora usata solo per visualizzare la homepage
@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route per gestire l'autenticazione
@api.route('/regok', methods=['GET'])
def index2():
    email = request.args.get('username')
    password = request.args.get('password')
    
    if email and password:
        email = email.lower()  # Normalizza l'email in minuscolo
        if email in utenti and utenti[email] == password:
            return render_template('reg_ok.html')
    
    return render_template('reg_ko.html')

# Route di errore di autenticazione (separata)
@api.route('/regko', methods=['GET'])
def index3():
    return render_template('reg_ko.html')

# Route per la registrazione di nuovi utenti
@api.route('/register', methods=['GET', 'POST'])
def index4():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        
        if email and password:
            email = email.lower()  # Normalizza l'email in minuscolo
            if email not in utenti:
                utenti[email] = password  # Aggiunge l'utente al dizionario
                return redirect(url_for('index2', username=email, password=password))
            else:
                return redirect(url_for('index3'))  # Se l'utente esiste già
    
    return render_template('registrati.html')

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=8085)
