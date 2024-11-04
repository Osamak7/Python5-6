import dbclient as db
cur = db.connect()

print("Quale operazioni desideri fare :")
print("         1 = Scrittura")
print("         2 = Lettura")
print("         3 = Exit")
ris = input("inserisci l'operazione :  ")

if ris == '3':
    print("Arrivederci")
elif ris == '2':
    sQuery = "select * from Utenti"
    db.read_in_db(cur, sQuery)
elif ris == '1':
    email = input("inserisci la mail: ")
    password = input(" inserisci la password: ")
    privilegi = input("insirisci i privilegi: ")
    note = input("inserisci una nota: ")
    sQuery = f"insert into utenti (email, password, privilegi, note)values('{email}', '{password}', '{privilegi}', '{note}')"
    db.write_in_db(cur , sQuery)
    print(f"hai aggiunto l'utente {email}")