op=0
lista=[]
while(op<=9):
    try:
        num=int(input("Digite um numero inteiro:"))
        num*=num
        lista.append(num)
        op+=1
    except ValueError:
        print("Digite um numero inteiro valido")
print(f"a soma do quadrado de todos os elementos da estrutura A é :{sum(lista)}")