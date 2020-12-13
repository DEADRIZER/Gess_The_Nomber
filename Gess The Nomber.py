#coding:utf-8

import random 
import time 

nombre_test = 0
jeux_lancé = False

démarage_jeux = input("voulez vous lancer le jeux ? > ")
if(démarage_jeux == "oui"):
	jeux_lancé = True

elif(démarage_jeux == "non"):
		print("aurevoir")

while jeux_lancé == True:
	print("welcome on the game \"Gess the nomber\"")
	nombre_a_deviner = random.randrange(1,101)
	print("")
	print("Le jeux consister à trouver le même nombre que l'ordinateur a en tête.")
	print("...")
	time.sleep(1)
	print("le nombre a deviner est comprit entre 1 et 100 inclue, bonne chance !")
	print("")

	while nombre_test != nombre_a_deviner:
		print("")
		nombre_test = input("tapez le nombre que vous pensez etre le bon > ")
		print("")

		if(nombre_test == ("")):
			continue

		else:
			nombre_test = int(nombre_test)

		print("...")
		time.sleep(1)
		if(nombre_test < nombre_a_deviner):
			print("le nombre a deviner est plus grand que celui que vous avez rentré")
			continue

		elif(nombre_test > nombre_a_deviner):
			print("le nombre a deviner est plus petit que celui que vous avez rentré")
			continue
		
		elif(nombre_test == nombre_a_deviner):
			print("bien joué vous avez trouvé le bon numéraux !")
			break
			
		elif(nombre_test > 100):
			print("le nombre a deviner est comprit entre 1 et 100")
			continue

	print("...")
	time.sleep(1)
		
	suite_de_la_partie = input("voulez voue continué a jouer ?")
		
	if(suite_de_la_partie == "oui"):
		continue
		
	elif(suite_de_la_partie == "non"):
		print("aurevoir")
		break

	else:
		print("requette introuvable !")




	
	








