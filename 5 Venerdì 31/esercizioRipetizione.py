lista_risultati = []

x = int(input("Quanti calcoli vuoi fare? "))
for i in range(x):


    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero"))

def addizione():
    return numero1 + numero2 

#chiedere all'utente quante volte vuole fare un calcolo


while x <= 0:
    print("Per favore ripeti, inserisci un valor valido")

    print("Che operazione vuoi fare?")
    print("+")
    print("-")
    print("*")
    print("/")
    scelta = input("+ - * / ")

    if scelta == "+":
        print(addizione)

    