op='1'
while(op!="0"):
    try:
        numero=int(input("Digite um numero inteiro"))
        print(f"o numero {numero} é par") if numero%2==0 else print(f"o numero {numero} é impar")
        op=input("digite 0 para sair")
    except ValueError:
        print("Erro Digite um numero valido inteiro")