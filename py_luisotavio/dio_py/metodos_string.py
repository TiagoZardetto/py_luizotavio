## pegará o valor de 'curso' e introduzir ao meio, no ARGUMENTO indica o range de índice 0 a 8 ---> 0 1 2 3 4 5 6 7  '#Python#' ##
curso = "Python"
print(curso.center(8, "#")) ##output: "#Python#"


## pegará o valor de 'curso' e dar ums 'join' (juntar) de Exclamações (!) entre o texto atribuído ---> P!y!t!h!o!n ##
curso = "Python"
print("!".join(curso)) ##output: "P!y!t!h!o!n"


## manipulando tamanho dos caracteres da string (nome), upperCase --> Letras MAIÚSCULAS // lowerCase --> Letras minúsculas // titleCase --> Como Texto certo (letra maiuscula começo)##
nome = "tiAgo"
print(nome.upper()) ##Output: TIAGO
print(nome.lower()) ##Output: tiago
print(nome.title()) ##Output: Tiago

## manipulando espaços em branco deixados pela string (nome), chamado de método STRIP, strip --> 'limpa' caracter em branco // lstrip --> leftstrip   // rstrip --> right strip ##

nome = "  Tiago   "
print(nome.strip()) #sem espaço em branco ("Tiago")
print(nome.lstrip()) #sem espaço branco na esquerda ("Tiago   ")
print(nome.rstrip()) #sem espaço branco na direita  ("  Tiago")