print('        Item      Código  Preço')
print(' Cachorro quente     1    10,00')
print('      Bauru          2    5,00')
print('    Hamburguer       3    13,00')
print('      Pastel         4    8,00')
print('   Refrigerante      5    4,00')
print('       Suco          6    7,00')
codigo = int(input('Digite o código do item que você deseja: '))
qtd = int(input('Quantos você deseja? '))
if codigo == 1:
    preco = 10
if codigo == 2:
    preco = 5
if codigo == 3:
    preco = 13
if codigo == 4:
    preco = 8
if codigo == 5:
    preco = 4
if codigo == 6:
    preco = 7
valor = preco*qtd
print('O valor que você irá pagar será de {} reais.'.format(valor))
