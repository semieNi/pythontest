faturamento_bruto = float(input('Digite o seu faturamento bruto:R$'))
custo_adm = float(input('Digite o seu custo administrativo:R$'))
aliquota_ipi = float(input('Digite a alíquota do IPI (%):'))
multiplicador_encargos = float(input('Digite o multiplicador de encargos:'))
folha_pagamento = float(input('Digite o valor da sua folha de pagamento:R$'))

impostos_producao = ((faturamento_bruto-custo_adm)*aliquota_ipi)/100
impostos_folha = folha_pagamento*multiplicador_encargos
custo_total_impostos = impostos_producao+impostos_folha

print('Seu custo total de impostos é: R$', custo_total_impostos)
