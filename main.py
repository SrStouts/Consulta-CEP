import requests
import os
import time


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('######################')
    print('#### Consulta CEP ####')
    print('######################\n')

    cep = input('Informe o CEP\n==> ')
    cep = cep.replace('-', '')
    cep = cep.replace('.', '')

    if cep == '':
        main()
    if cep.isnumeric():
        pass
    else:
        print('Digite apenas números.')
        time.sleep(2)
        main()
    if len(cep) != 8:
        print('O CEP precisa ter 8 digítos.') 
        time.sleep(2)
        main()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    result = request.json()
    
    
    if 'erro' not in result:
        print('---------------------------------------')
        print('==> CEP Encontrado <==')
        print('CEP: {}'.format(result['cep'] or 'Dados não encontrado.'))
        print('Logradouro: {}'.format(result['logradouro'] or 'Dados não encontrado.'))
        print('Bairro: {}'.format(result['bairro'] or 'Dados não encontrado.'))
        print('Cidade: {}'.format(result['localidade'] or 'Dados não encontrado.'))
        print('Estado: {}'.format(result['uf'] or 'Dados não encontrado.'))
        print('---------------------------------------')
    else:
        print('CEP não encontrado.')
        print('---------------------------------------')

    try:
        op = int(input('Deseja fazer uma nova consulta?\n1. Sim\n2. Sair\n==> '))
    
        if op == 1:
            time.sleep(1)
            main()
        elif op == 2:
            print('Saindo...')
            time.sleep(1)
            exit()
        else:
            print('Opção inválida, saindo...')
            time.sleep(1)
            exit()
    except ValueError:
        print('Aí é foda, tu não tá vendo as opções não? Só por isso eu vou sair...')       
        time.sleep(4)


if __name__ == '__main__':
    main()
