from frota import *
def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))


        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(Carro)

if __name__ == "__main__":
    print('Cadastre um carro1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    km = float(input('Digite a quilometragem: '))
    nm_tanque = float(input('Digite a capacidade do tanque: '))
    nm_cm = float(input('Digite o consumo medio do carro: '))
    carro1 = Carro(nm_modelo, nm_marca, nm_cor, nm_tanque, nm_cm, 0, False)

    print('Cadastre um carro2')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    km = float(input('Digite a quilometragem: '))
    nm_tanque = float(input('Digite a capacidade do tanque: '))
    nm_cm = float(input('Digite o consumo medio do carro: '))
    carro2 = Carro(nm_modelo, nm_marca, nm_cor, nm_tanque, nm_cm, 0, False)


    '''
    Controlando o carro até ele atingir 600 Km
    '''

    while carro1.odometro < 600 and carro2.odometro < 600 and (carro1.tanque > 0 or carro2.tanque > 0) :

        try:
            op_carro = 0
            while op_carro not in (1, 2):
                op_carro = int(input('Qual carro voce deseja controlar?'))

            if op_carro == 1:
                operar_carro(carro1)
            if op_carro == 2:
                operar_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()

    print(carro1)
    print(carro2)

    if carro2.odometro > carro1.odometro or carro1.tanque <= 0:
        print('carro 2 venceu')
    else:
        print('carro 1 venceu')

    print('Parar para trocar o óleo dos carros!!!')

