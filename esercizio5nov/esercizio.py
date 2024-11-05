import dbclient as db
cur = db.connect()

print("Quale operazioni desideri fare :")
print("         1 = Scrittura")
print("         2 = Lettura")
print("         3 = Exit")
result = input("inserisci l'operazione :  ")

while result != '3':
    
    if result == '2':
        sQuery = input("inserisci la query che desideri in lettura:\n")
        ret = db.read_in_db(cur, sQuery)

        if (ret == -1):
            print("hai inserito una query non valida \n")
        else:
            print("Query eseguita correttamente\n")

    elif result == '1':
        sQuery = input("inserisci la query che desideri in scrittura:\n")
        ret = db.write_in_db(cur,sQuery)

        if (ret == 0):
            print("Query eseguita correttamente")
        else:
            print("hai inserito una query non valida \n")
        


    else:
        print("\nhai inserito un' operazione sbagliata")
        print("Quale operazioni desideri fare :")
        print("         1 = Scrittura")
        print("         2 = Lettura")
        print("         3 = Exit")
        
    result = input("inserisci l'operazione :  ")