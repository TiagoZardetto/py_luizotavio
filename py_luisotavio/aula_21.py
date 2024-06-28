## Usando formats de outro jeito ##

a = 'AAAAAA'
b = 'BBBBB'
c = 1.78

# Output disto será: a{} b{} c{}
##string = 'a={} b={} c={}'##
##print(string)##

## Agora usando o método format, irá mostrar os valores de acordo com a ordem dos mesmos. ##
## Output = 
string = 'a={} b={} c={}'
formato = string.format(a, b, c)

print(formato)