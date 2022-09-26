excesso=[]
cont=0
index=[]
op=None
multa=0
while(op!="0"):
    try:
        peso=float(input("Digite o peso do peixe"))
        if peso - 50 <= 0:
            print("o peixe nao teve excesso")
        else :
            excesso.append(peso-50)
            multa+=((peso-50)*4)
            index.append(cont)
            print(f"o excesso foi de {peso-50}")
        op=input("se deseja continuar nao digite 0:")
        cont+=1
    except ValueError:
        print("valor Invalido")
for i in range(len(excesso)):
    print(f"Peixe numero {index[i]+1} teve {excesso[i]} de peso a mais ")
print(f"valor da multa:{multa}")
input("digite enter para finalizar:")