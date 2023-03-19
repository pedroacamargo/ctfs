def menu():
    print("\033[1;33;40m--------------------\033[0m")
    print("\033[1;34;40m1: Somar")
    print("2: Subtrair")
    print("3: Multiplicar")
    print("4: Sair\033[0m")
    print("\033[1;33;40m--------------------\033[0m")

def somar(a,b):
    print(f'\033[1;31;40m{a} + {b} = {a + b}\033[0m')

def subtrair(a,b):
    print(f'\033[1;31;40m{a} - {b} = {a - b}\033[0m')

def multiplicar(a,b):
    print(f'\033[1;31;40m{a} * {b} = {a * b}\033[0m')

while True:
    menu()
    escolha = int(input("Digite uma função: "))
    if escolha == 1:
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        somar(n1,n2)
    elif escolha == 2:
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        subtrair(n1, n2)
    elif escolha == 3:
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        multiplicar(n1,n2)
    elif escolha == 4:
        break;
    else:
        print("Por favor, digite um valor válido.")
