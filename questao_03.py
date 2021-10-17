salario = 1200
conta1 = 200
conta2 = 120

jurosc1 = (2/100)*conta1
jurosc2 = (2/100)*conta2

divida = conta1+conta2+jurosc1+jurosc2

salariofinal = float(salario-divida)

print('O restentante do seu salário é: R$', salariofinal)