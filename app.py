from modelos.restaurante import Restaurante

restaurante_belgrano = Restaurante('Belgrano', 'Pizzaria')
restaurante_soushi = Restaurante('Soushi', 'Japonesa')
restaurante_belvedere = Restaurante('Belvedere', 'Lanches')

restaurante_belgrano.receber_avaliacao('Pablo', 2)
restaurante_belgrano.receber_avaliacao('Rodrigo', 5)
restaurante_belgrano.receber_avaliacao('Ana', 2)
restaurante_belgrano.receber_avaliacao('Mona', 4)

restaurante_soushi.receber_avaliacao('Julio', 1)
restaurante_soushi.receber_avaliacao('Magali', 10)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()