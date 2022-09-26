op='1'
while(op!="0"):
    try:
        numero=float(input("Digite um numero"))
        print(f"o numero {int(numero)} é inteiro") if numero%1==0 else print(f"o numero {numero} é dicimal")
        op=input("digite 0 para sair")
    except ValueError:
        print("Erro Digite um numero valido")