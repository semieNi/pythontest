valor_produto = float(input("Digite o valor de venda unitário do seu produto (R$):"))
quantidade_produto = int(input("Digite a quantidade de produto a ser comprada:"))
aliquota_icms = float(input("Digite a alíquota do ICMS (%):"))

imposto_pago = (valor_produto*quantidade_produto*aliquota_icms)/100
preco_total = valor_produto*quantidade_produto+imposto_pago

print("O valor total da sua venda é de: R${} e o valor total de imposto é: R${}".format(preco_total,imposto_pago))