
## Leitor de Código de Barras

Desafio Leitor de código Loggi. Um software que identifica e separa os códigos de barra, seguindo algumas diretrizes: 

* Identificar pacotes válidos e invalidos.
* Não sendo possível despachar pacotes contendo jóias tendo como região de origem o Centro-oeste.
* Não envia produtos que não sejam dos tipos informados.
* Não envia produtos de vendedores inativos.
* Identificar o destino de cada pacote.
* Identificar se algum pacote que tem como origem a região Sul tem Brinquedos em seu conteúdo.
* Listar os pacotes agrupados por região de destino.
* Listar o número de pacotes enviados por cada vendedor.
* Gerar o relatório/lista de pacotes por destino e por tipo.

## Abordagem

Os códigos de barra são e devem ser armazenados no arquivo `barcode.txt`

O software não faz validação dos códigos, então os códigos armazenados **devem** ser apenas números contendo 15 digitos.

#### Exemplo:
      
    Código: 888333555999000 
    
#### Para rodar, execute:

    python barcode.py

