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

sellersNotAvailable = ['584']
validBarcode = []
sellers = {}

def add_sellers(code):
    validBarcode.append(code)
    if code[9:12] not in sellers:
        sellers[code[9:12]] = 1
    else:
        sellers[code[9:12]] += 1

def show_information(code):
    screenCode = '{} {} {} {} {}'.format(code[:3], code[3:6], code[6:9], code[9:12], code[12:])
    print('Código: ', screenCode)
    print('Região de origem: ', region[code[:3]])
    print('Região de destino: ', region[code[3:6]])
    print('Tipo de produto: ', productType[code[12:]])

def show_invalid_information(code):
    screenCode = '{} {} {} {} {}'.format(code[:3], code[3:6], code[6:9], code[9:12], code[12:])
    print('O Código: ', screenCode)
    print('É um código inválido')

def show_invalid_from_centro(code):
    screenCode = '{} {} {} {} {}'.format(code[:3], code[3:6], code[6:9], code[9:12], code[12:])
    print('O Código: ', screenCode)
    print('Não é possível despachar pacotes contendo joías tendo como região de origem o Centro-oeste')

def destination_and_type():
    for i in region:
        print('Região: ', region[i])
        for j in productType:
            empty = 0
            print('   ', productType[j], ':')
            for k in range(0,len(validBarcode)):
                if i == validBarcode[k][3:6] and j == validBarcode[k][12:]:
                    screenCode = '{} {} {} {} {}'.format(validBarcode[k][:3], validBarcode[k][3:6], validBarcode[k][6:9], validBarcode[k][9:12], validBarcode[k][12:])
                    print('     - ', screenCode)
                    empty = 1
            if not empty:
                print('     - Não estão sendo enviado', productType[j], 'para a região', region[i])
        print()

def sent_by_sellers():
    for i in sellers:
        print()
        print('Código do vendedor: ', i)
        print('Número de pacotes enviados: ', sellers[i])

def region_destintion():
    for i in region:
        print()
        print(region[i],':')
        for j in range(0,len(validBarcode)):
            if i == validBarcode[j][3:6]:
                screenCode = '{} {} {} {} {}'.format(validBarcode[j][:3], validBarcode[j][3:6], validBarcode[j][6:9], validBarcode[j][9:12], validBarcode[j][12:])
                print(' - ', screenCode)


def barcode_reader(code):
    print()
    if code[:3] not in region or code[12:] not in productType or code[9:12] in sellersNotAvailable:
        show_invalid_information(code)
    elif code[:3] == '111' and code[12:] == '000':
        show_invalid_from_centro(code)
    elif code[:3] == '000' and code[12:] == '888':
        print('\nContém brinquedo de origem da Região Sul')
        show_information(code)
        add_sellers(code) 
    else:
        show_information(code)
        add_sellers(code)


if __name__ == '__main__':
    while True:
        print()
        print('1 - Ler arquivo BarCode.txt')
        print('2 - Listar por região de destino')
        print('3 - Listar o número de pacotes enviados por cada vendedor')
        print('4 - Listar por destino e por tipo')
        option = int(input('Qual a opção?: '))
        if option == 1:
            barcode = open('barcode.txt', 'r')
            for line in barcode:
                barcode_reader(line[:-1])
        elif option == 2:
            if validBarcode:
                region_destintion()
            else:
                print('\nCódigo de barras válidos vazio')
        elif option == 3:
            if sellers:
                sent_by_sellers()
            else:
                print('\nVendedores vázios')
        elif option == 4:
            if validBarcode:
                destination_and_type()
            else:
                print('\nCódigo de barras válidos vazio')