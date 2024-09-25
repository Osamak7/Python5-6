from flask import Flask , render_template , request

api = Flask(__name__)

utenti :dict[str , str] = {
            "mario@777.it":"rossi", 
            "gianni@12.it" : "derossi", 
            "anita@123.com" : "garibaldi"
            }

@api.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def index2():
    email = request.args.get('username')
    password = request.args.get('password')
    email = email.lower()
    
    if email in utenti and password == utenti[email]:
        return render_template('reg_ok.html')
    else:
        return render_template('reg_ko.html')


@api.route('/regko', methods=['GET'])
def index3():
     
    return render_template('reg_ko.html')

@api.route('/register', methods=['GET'])
def index4():
    email = request.args.get('username')
    password = request.args.get('password')
    if email in utenti:
        return render_template('registrati.html')
    else:
        utenti[email]=password
        return render_template('reg_ok.html')
    

api.run(host="0.0.0.0",port=8085)