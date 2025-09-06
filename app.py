from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_belgrano = Restaurante('Belgrano', 'Pizzaria')
restaurante_soushi = Restaurante('Soushi', 'Japonesa')
restaurante_belvedere = Restaurante('Belvedere', 'Lanches')

prato1 = Prato('Pizza Margherita', 30, 'Pizza clássica com molho de tomate e queijo')
bebida1 = Bebida('Coca-Cola', 10, '350ml')

prato1.aplicar_desconto(10)

restaurante_belgrano.adicionar_item_ao_cardapio(prato1)
restaurante_belgrano.adicionar_item_ao_cardapio(bebida1)

def main():
    restaurante_belgrano.listar_cardapio()


if __name__ == '__main__':
    main()