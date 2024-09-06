import os

def CercaStringaInNomeFile(sFile , sStringa):
    strLower = sStringa.lower()
    fileLower = sFile.lower()
    result = True if (fileLower.find(strLower)>=0) else False
    return result

def cercaStringaInContenutoFile(parola , rootFile):
    return False


sRoot = input("inserisci la root directory: ")
sParola = input("inserisci la parola da cercare: ")
sOutDir = input("inserisci directori di output: ")
nfileTrovati = 0

for root , dirs, files in os.walk(sRoot):
    print(f"sto guardando {root} che contiene { len(dirs)} sub directory e {len(files)} files") 

    for file in files:
        
        print(f"Devo vedere se {file} contiene {sParola}")
        bret = CercaStringaInNomeFile(file,sParola)
        
        if bret == True :
            nfileTrovati += 1 
        
        else :
            sFilepath = os.patch.join(root,file)
            bret = cercaStringaInContenutoFile(sParola, sFilepath)
            if(bret == True):
                pass

print(f"ho trovato {nfileTrovati} file con la parola {sParola}")