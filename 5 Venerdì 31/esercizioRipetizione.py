def addizione(numero1, numero2):
        return numero1 + numero2 

lista_risultati = []

x = int(input("Quanti calcoli vuoi fare? "))
for i in range(x):


    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero "))

#chiedere all'utente quante volte vuole fare un calcolo
    while x <= 0:
        print("Per favore ripeti, inserisci un valor valido")

#chiedere all'utente che tipo di operazione vuole fare attraverso un menù
    print("Che operazione vuoi fare?")
    print("+")
    print("-")
    print("*")
    print("/")
    scelta = input("+ - * / ")

    if scelta == "+":
       risultato = addizione(numero1, numero2)
       lista_risultati.append(risultato)

    