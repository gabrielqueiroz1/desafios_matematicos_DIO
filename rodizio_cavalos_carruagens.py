n = int(input())
while n != 0:
    placa = input().split("-")
    placa_inicial = placa[0].upper()
    if len(placa[0]) == 3 and placa[0] == placa_inicial and placa[0] is not int and len(placa[1]) == 4 and placa[1] is not str:
        last_number = int(placa[1][3])
        if last_number == 1 or last_number == 2:
            print("SEGUNDA")
        elif last_number == 3 or last_number == 4:
            print("TERCA")
        elif last_number == 5 or last_number == 6:
            print("QUARTA")
        elif last_number == 7 or last_number == 8:
            print("QUINTA")
        elif last_number == 9 or last_number == 0:
            print("SEXTA")
    else:
        print("FALHA")
    n -= 1
