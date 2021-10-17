# Calculadora

n1 = float(input('Digite o primeiro número:'))
op = input('Digite uma operação (+,-,/,*):')
n2 = float(input('Digite o segundo número:'))

if (op == '+'):
        resultado = n1 + n2
elif (op == '-'):
    resultado = n1 - n2
elif (op == '/'):
    resultado = n1 / n2
elif (op == '*'):
    resultado = n1 * n2
else:
    resultado = 'Falha na operação.'
    
print(n1,op,n2,'=',resultado)