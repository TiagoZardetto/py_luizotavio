nome = 'Tiago Zardetto'
altura = 1.72
peso = 75
imc = peso / (altura ** 2) 

## calculando IMC e mostrando no Terminal ##
linha_1 = f'{nome} tem {altura} e pesa {peso:.1f} atualmente'
linha_2 = f'{nome} tem um imc de: {imc:.2f} atualmente, ta gordin'
linha_3 = f'{nome} tem uma altura de: {altura}'

print(linha_1)
print(linha_2)
print(linha_3)

