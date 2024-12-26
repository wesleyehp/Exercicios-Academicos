sal_carlos = float(input('Digite o valor do salário de Carlos R$: '))
sal_joao = sal_carlos / 3
meses = 0
while (sal_joao < sal_carlos):
    sal_carlos = sal_carlos + (sal_carlos * (2/100))
    sal_joao = sal_joao + (sal_joao * (5/100))
    meses += 1
print('Demorou {} meses para que o salário de João ultrapassase o de Carlos:'.format(meses))
print('Salário de Carlos no final R${:.2f}'.format(sal_carlos))
print('Salário de João no final R${:.2f}'.format(sal_joao))