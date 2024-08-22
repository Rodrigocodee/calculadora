def somar (x, y):
    return  x + y

def adicao (x, y):
    return x - y

def multiplicacao (x, y):
    return x * y

def divisao (x, y):
    if divisao != 0:
        return x / y
    else: 
        print('Erro! divisao igual a 0')


def calculadora ():
    print('Escolha a seguinte operação: ')
    print('1 - soma')
    print('2 - adição')
    print('3 - multiplicação')
    print('4 - divisão')

    escolha = input('Escolha as seguintes das operações (1/2/3/4): ')

    if escolha in ['1', '2', '3', '4']:
        num_1 = int(input('Digite um numero: '))
        num_2 = int(input('Digite outro numero: '))

        if escolha == '1':
            print(f'{num_1} + {num_2} = {somar(num_1,num_2)}')
        
        elif escolha == '2':
            print(f'{num_1} - {num_2} = {adicao(num_1, num_2)}')
        
        elif escolha == '3':
            print(f'{num_1} * {num_2} = {multiplicacao(num_1,num_2)}')
        
        elif escolha == '4':
            print(f'{num_1} / {num_2} = {divisao(num_1, num_2)}')

        else: 
            print('Erro!')

calculadora()