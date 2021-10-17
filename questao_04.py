salariobruto = float(input('Digite o seu salário bruto (R$):'))
aliquota_inss = float(input('Digite a alíquota do seu INSS (%):'))
aliquota_ir = float(input('Digite a alíquota do IR (%):'))
redutor_ir = float(input('Digite o redutor do IR (R$):'))

valor_inss = (salariobruto*aliquota_inss)/100
valor_ir = ((salariobruto-valor_inss)*aliquota_ir)/100 - redutor_ir
salario_liquido = salariobruto-valor_inss-valor_ir

print('Seu salário líquido é: R${}, o valor do IR é: R${} e o valor do INSS é: R${}'.format(salario_liquido,valor_ir,valor_inss))