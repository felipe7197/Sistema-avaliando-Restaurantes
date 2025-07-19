from modelos.restaurante import Restaurante


restaurante_praça = Restaurante  ('Praça','Gourmet')
restaurante_praça.receber_avaliacao('Felipe', 10)
restaurante_praça.receber_avaliacao('Jorge', 5)
restaurante_praça.receber_avaliacao('Luana', 8)
restaurante_praça.receber_avaliacao('Pablo', 2)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()