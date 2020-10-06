
#ouvrir un fichier en mode lecture
fichier = open("monfichier.txt",'r')
contenu = fichier.read() 
print(contenu)
fichier.close()