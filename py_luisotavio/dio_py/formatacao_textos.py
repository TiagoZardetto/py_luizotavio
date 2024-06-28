## Formatar textos ---> letra “f” antes do texto e colocando a sua variável dentro de {} chaves ##
nome = "Tiago"
print(f"O {nome} não está composto dentro de nosso Banco de Dados")#

idade = 21
print(f"Tem a idade igual a: {idade}")

print(f"O usuário {nome} que pratica Basquete, tem {idade} anos de idade...")#


## Formantando números com casas decimais para exibir ao usuário ##
faturamento = 1000
print(f"Faturamento mensal de: {faturamento: .2f}")
print(f"Faturamento mensal de: R${faturamento: .3f} doláres...")

margem_lucro = 0.27
print(f"Margem de lucro está entre: {margem_lucro:.1%}!")
print("Bom dia a todos os colaboradores, enviando Faturamento e Margem de Lucro mensal...")
print(f"Faturamento mensal = R${faturamento: .2f}!")
print(f"Margem de Erro = {margem_lucro: .1%}!")

## Formatando texto ---> {Format}
print("Olá me chamo {1} e tenho atualmente {0} anos de idade!".format(idade, nome))
print("Boa Tarde me chamo{3}, minha empresa atual tem um faturamento de R${0} e uma margem de lucro de:{1}; acabei de completar{2}anos de idade!".format(faturamento, margem_lucro, idade, nome))