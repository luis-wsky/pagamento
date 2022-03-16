# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('-'*30)
print('{:^27}'.format('LOJAS LAW'))
print('-'*30)
valor = float(input('Digite o valor em R$: de suas compras:'))
print('''Como deseja pagar?
[ 1 ] a vista com 10% de desconto:
[ 2 ] a vista no cartão de crétido com 5% de desconto:
[ 3 ] em duas vezes no cartão de crétido:
[ 4 ] em três vezes no cartão de crédito:''')
opcao = int(input('Qual é a opção desejada?'))
if opcao == 1:
    desconto = valor * (10/100)
    total = valor - desconto
    print('O total ficou em R$: {:.2f}'.format(total))
elif opcao == 2:
    desconto2 = valor * (5/100)
    total2 = valor - desconto2
    print('O total ficou em R$: {:.2f}'.format(total2))
elif opcao == 3:
    parcela = valor / 2
    print('O total ficou em R$: {:.2f}'.format(parcela))
elif opcao == 4:
    parcela2 = valor * (20/100)
    total3 = valor + parcela2
    total4 = (valor + parcela2)/(3)
    print('O total ficou em {:.2f} dividido em 3x de R$: {:.2f}'.format(total3, total4))
else:
    print('\033[30;41m --- OPÇÃO INVÁLIDA, TENTE NOVAMENTE: ---\033[m')
