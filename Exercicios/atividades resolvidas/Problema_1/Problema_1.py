#Q29- Foi feita uma pesquisa entre habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa que calcule e mostre:
#a)A média dos salários do grupo: *
#b) A maior e a menor idade do grupo: *
#c) A quantidade de mulheres com o salário até R$ 200,00 *
#d) A idade e o sexo da pessoa que possui o menor salário *
#Fizaline a entrada de dados ao ser digitada uma idade negativa*

idade = qntd = feminino = maioridade = menoridade = menorsalario  = media = salarioidade = salariosexo = salarios = 0
print('{}=+==+==+==+==+==+==+==+==+==+==+==+='.format('\033[0;32m'))
print('=Pesquisa entre habitantes regional=')
print('=+==+==+==+==+==+==+==+==+==+==+==+={}'.format('\033[m'))
while idade >= 0:
    idade = int(input('\n{}Digite a sua idade: '.format('\033[0;36m')))
    if idade < 0:
        break
    sexo = str(input('Informe o seu sexo (M/F): ')).upper()
    salario = float(input('Digite o valor do seu salário R$'))
    salarios += salario
    qntd += 1
    if qntd == 1:
        maioridade = menoridade = idade
    elif idade > maioridade:
        maioridade = idade
    elif idade < menoridade:
        menoridade = idade
    
    if qntd == 1:
        menorsalario = salario
        salarioidade = idade
        salariosexo = sexo
    else:
        if salario < menorsalario:
            menorsalario = salario
            salarioidade = idade
            salariosexo = sexo
    
    if sexo == ('F') and salario <= 200:
        feminino += 1
    media = (salarios) / qntd
    print('\n{}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{}'.format('\033[0;31;40m', '\033[m'))
    print('{}!Se desejar parar o programa digite uma idade negativa!{}'.format('\033[0;31;40m', '\033[m'))
    print('{}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{}'.format('\033[0;31;40m', '\033[m'))

print('\n{}==========================================================={}'.format('\033[0;32;40m', '\033[m'))
print('{}A média de salário desse grupo é R${:.2f}{}'.format('\033[0;32;40m', media, '\033[m')) #A    
print('{}A maior idade desse grupo é {} e a menor é {}{}'.format('\033[0;32;40m', maioridade, menoridade, '\033[m')) #B
print('{}Nesse grupo possui {} mulheres com o salário até R$200,00{}'.format('\033[0;32;40m', feminino, '\033[m')) #C
print('{}A pessoa que tem o menor salário tem {} anos e é do sexo {}{}'.format('\033[0;32;40m', salarioidade, salariosexo, '\033[m')) #D
print('{}==========================================================={}'.format('\033[0;32;40m', '\033[m'))
