#Diionarios com informações da regiao e produto.
region = {
    '111' : 'Centro-oeste',
    '333' : 'Nordeste',
    '555' : 'Norte',
    '888' : 'Sudeste',
    '000' : 'Sul'
}

productType = {
    '000' : 'Jóias',
    '111' : 'Livros',
    '333' : 'Eletrônicos',
    '555' : 'Bebidas',
    '888' : 'Brinquedos'
}

#Lista para vendedores que não estejam permitidos.
sellersNotAvailable = ['584']
#Armazena os códigos de barra válidos.
validBarcode = []
#Dicionario para contar envio de cada vendedor.
sellers = {}

#Fução que adiciona os códigos válidos e conta os envios de cada vendedor.
def add_sellers(code):
    if code not in validBarcode: #verifica se o código de barra já foi adicionado na lista.
        validBarcode.append(code)

    if code[9:12] not in sellers:
        sellers[code[9:12]] = 1
    else:
        sellers[code[9:12]] += 1

#Fução para exibir a informações válidas dos códigos de barra informado.
def show_information(code):
    screenCode = '{} {} {} {} {}'.format(code[:3], code[3:6], code[6:9], code[9:12], code[12:]) #Apenas para ter uma exibição mais agradável :D
    print('Código: ', screenCode)
    print('Região de origem: ', region[code[:3]])
    print('Região de destino: ', region[code[3:6]])
    print('Tipo de produto: ', productType[code[12:]])

#Fução para exibir a informação "não válida" do o código de barra informado.
def show_invalid_information(code):
    screenCode = '{} {} {} {} {}'.format(code[:3], code[3:6], code[6:9], code[9:12], code[12:])
    print('O Código: ', screenCode)
    print('É um código inválido')

#Fução para exibir a informação "não válida" ao despachar pacotes contendo joías e sendo da regiao Centro-Oeste.
def show_invalid_from_centro(code):
    screenCode = '{} {} {} {} {}'.format(code[:3], code[3:6], code[6:9], code[9:12], code[12:])
    print('O Código: ', screenCode)
    print('Não é possível despachar pacotes contendo joías tendo como região de origem o Centro-oeste')

#Função para ordenar e exibir por Região de destino e tipo de produto.
def destination_and_type():
    for i in region:
        print('Região: ', region[i])
        for j in productType:
            empty = 0   ##Variável para verificar se entrou na condição, caso não, exibe uma mensagem.
            print('   ', productType[j], ':')
            for k in range(0,len(validBarcode)):
                if i == validBarcode[k][3:6] and j == validBarcode[k][12:]:
                    screenCode = '{} {} {} {} {}'.format(validBarcode[k][:3], validBarcode[k][3:6], validBarcode[k][6:9], validBarcode[k][9:12], validBarcode[k][12:])
                    print('     - ', screenCode)
                    empty = 1
            if not empty:
                print('     - Não estão sendo enviado', productType[j], 'para a região', region[i])
        print()

#Função para exibir quantos envios foram feitos para cada vendedor.
def sent_by_sellers():
    for i in sellers:
        print()
        print('Código do vendedor: ', i)
        print('Número de pacotes enviados: ', sellers[i])

#Função para ordenar e exibir por região de destino.
def region_destintion():
    for i in region:
        print()
        print(region[i],':')
        for j in range(0,len(validBarcode)):
            if i == validBarcode[j][3:6]:
                screenCode = '{} {} {} {} {}'.format(validBarcode[j][:3], validBarcode[j][3:6], validBarcode[j][6:9], validBarcode[j][9:12], validBarcode[j][12:])
                print(' - ', screenCode)

#Função que verifica e valida o código de barra.
def barcode_reader(code):
    print()
    if code[:3] not in region or code[12:] not in productType or code[9:12] in sellersNotAvailable: #Verifica se os produtos existem no banco e se o vendedor está inativo.
        show_invalid_information(code)
    elif code[:3] == '111' and code[12:] == '000': #Verifica se está sendo enviado joiás do Centro-Oeste.
        show_invalid_from_centro(code)
    elif code[:3] == '000' and code[12:] == '888': #Verifica se contém brinquendo de origem da Região Sul.
        print('\nContém brinquedo de origem da Região Sul')
        show_information(code)
        add_sellers(code) 
    else:
        show_information(code)
        add_sellers(code)

#main
def main():
    while True: #menu
        print()
        print('1 - Ler arquivo BarCode.txt')
        print('2 - Listar por região de destino')
        print('3 - Listar o número de pacotes enviados por cada vendedor')
        print('4 - Listar por destino e por tipo')
        option = int(input('Qual a opção?: '))

        #Analisando as opções escolhidas.
        if option == 1: 
            barcode = open('barcode.txt', 'r') #lendo arvo .txt
            for line in barcode: #percorrendo cada linha.
                barcode_reader(line[:-1]) 
        elif option == 2:
            if validBarcode: #verifica se não está vazio a lista de códigos de barra. 
                region_destintion()
            else:
                print('\nCódigo de barras válidos vazio')
        elif option == 3:
            if sellers: #verifica se não está vazio o dicionário de vendedores.
                sent_by_sellers()
            else:
                print('\nVendedores vázios')
        elif option == 4:
            if validBarcode: #verifica se não está vazio a lista de códigos de barra.
                destination_and_type()
            else:
                print('\nCódigo de barras válidos vazio')

if __name__ == '__main__':
    main()