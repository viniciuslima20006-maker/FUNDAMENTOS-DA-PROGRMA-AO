idade=18
salario=2000
tempo= 2


if idade >= 18 and salario >= 5000 and tempo >= 2:
    print("Empréstimo aprovado automaticamente.")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo} anos de trabalho — todas as condições básicas foram atendidas, portanto o empréstimo é aprovado automativcamente.")

elif idade >= 18 and (salario >= 2000 and tempo >= 2):
    print("Empréstimo aprovado")
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo} anos de trabalho — todas as condições básicas foram atendidas, portanto o empréstimo é aprovado normalmente.")
else: 

    print ("empréstimo negado pois nao atende os requisitos minimos ")

   
   
   

 
 

 