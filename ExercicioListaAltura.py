lista=[]
cont=0
op="1"
nomes=[]
while(op!="0"):
    try:
        nome=input("Digite seu nome:")
        nomes.append(nome)
        h=float(input("Digite sua altura:"))
        resp = input("Digite o sexo Masculino(M) ou Feminino(F) :")
        match resp.upper():
            case "F":
                lista.append((62.1 * h) - 44.7)
                print(f"seu peso ideal é {lista[cont]}")
            case "M":
                lista.append((72.7 * h) - 58)
                print(f"seu peso ideal é {lista[cont]}")
        op=input("se deseja continuar nao digite 0:")
        cont+=1
    except ValueError:
        print("valor Invalido")
for i in range(len(nomes)):
    print(f"{nomes[i]} seu peso ideal é {lista[i]}")
input("digite enter para continuar:")
