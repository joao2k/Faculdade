salarioBruto=[]
impostoDeRenda=[]
inss=[]
sindicado=[]
op="1"
cont=0
while(op!="0"):
    try:
        valorHora=float(input("valor da sua hora trabalhada:"))
        horas = float(input("Quantas horas trabalhadas por mes:"))
        salarioBruto.append(valorHora*horas)
        inss.append(salarioBruto[cont]*0.08)
        sindicado.append(salarioBruto[cont]*0.05)
        impostoDeRenda.append(salarioBruto[cont]*0.11)
        op=input("digite 0 para terminar de cadastrar todos:")
        cont+=1
    except ValueError:
        print("Valor invalido:")
for i in range(len(salarioBruto)):
     print(f"{i+1} pessoa Cadastrada:\n+Salário Bruto:{salarioBruto[i]}\nIR:{impostoDeRenda[i]}\n INSS:{inss[i]}\nSindicato:{sindicado[i]}\n ")
     print(f"Salário Liquido{(sindicado[i]+impostoDeRenda[i]+inss[i])-salarioBruto[i]}")
     input("aperte ENTER para finalizar")