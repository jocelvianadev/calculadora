"""
JOCEL VIANA EM 10/04/2024
Este é um projeto de uma calculadora que pede ao usuário dois números e pede também que o mesmo 
digite a operação a ser feita. O projeto valida todas as entradas do usuário.
"""
while True:
    numero1 = input('Informe o primeiro número: ')
    numero2 = input('Informe o segundo número: ')
    operador =  input('Informe uma das operações (+ - * /): ')

    numeros_validos = None
    numero1_float = 0
    numero2_float = 0

    ####################################################################################
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
    ####################################################################################

    if numeros_validos is None:
        print('Algum(s) (dos) número(s) informado(s) está(ão) errado(s)!')
        continue

    ####################################################################################

    operadores_permitidos = ['+', '-', '/', '*']

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Informe apenas 1 operador.')
        continue

    ####################################################################################

    print('Resultado:')

    if operador == '+':
        print(f'{numero1_float} + {numero2_float} = {numero1_float + numero2_float:.2f}')
    if operador == '-':
        print(f'{numero1_float} - {numero2_float} = {numero1_float - numero2_float:.2f}')
    if operador == '/':
        print(f'{numero1_float} ÷ {numero2_float} = {numero1_float / numero2_float:.2f}')
    if operador == '*':
        print(f'{numero1_float} x {numero2_float} = {numero1_float * numero2_float:.2f}')

    ####################################################################################
    # Encerrando a operação
    sair = input('Deseja sair? S/N: ').lower().startswith('s')
    if sair is True:
        break





