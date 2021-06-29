def barcode_reader(code):
    screenCode = '{} {} {} {} {}'.format(code[:3], code[3:6], code[6:9], code[9:12], code[12:])

    region = {
        '111' : 'Centro-oeste',
        '333' : 'Nordeste',
        '555' : 'Norte',
        '888' : 'Sudeste',
        '000' : 'Sul'
    }

    product_type = {
        '000' : 'Jóias',
        '111' : 'Livros',
        '333' : 'Eletrônicos',
        '555' : 'Bebidas',
        '888' : 'Brinquedos'
    }

    if code[:3] not in region or code[12:] not in product_type or code[9:12] == '584':
        print('Código inválido')
    elif code[:3] == '111' and code[12:] == '000':
        print('Não é possível despachar pacotes contendo joías tendo como região de origem o Centro-oeste')

    print()
    print('Código: ', screenCode)
    print(code[:])
    print(type(code))

if __name__ == '__main__':
    code = input('Digite o código: ')
    if len(code) == 15:
        barcode_reader(code)
    else:
        print('O código informado deve conter 15 dígitos')    
