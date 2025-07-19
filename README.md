# Sistema-avaliando-Restaurantes
Este projeto é um sistema simples de gerenciamento e avaliação de restaurantes desenvolvido em Python. Ele permite criar restaurantes, alternar seu status (ativo/inativo), receber avaliações de clientes e listar os restaurantes com suas informações.

Estrutura do Projeto

app.py é Arquivo principal de execução
modelos/ pasta onde está outras partes do projeto
restaurante.py - Classe Restaurante com lógica de negócio
avaliacao.py - Classe Avaliacao para clientes

Funcionamento
 restaurante.py
Contém a definição da classe Restaurante, com os seguintes recursos:

Atributos:

_nome e _categoria: armazenam dados do restaurante.

_ativo: indica se o restaurante está ativo ou não.

_avaliacao: lista com as avaliações recebidas.

restaurantes: classe lista com todos os restaurantes criados.

Métodos:

__str__(): retorna uma representação em string do restaurante.

listar_restaurantes(): exibe todos os restaurantes cadastrados com nome, categoria, média de avaliações e status.

ativo: retorna uma visualização do estado do restaurante (☒ ativo, ☐ inativo).

alternar_estado(): muda o status de ativo para inativo e vice-versa.

receber_avaliacao(cliente, nota): armazena uma nova avaliação se a nota estiver entre 1 e 5.

media_avaliacoes: calcula a média das notas recebidas.


🔹 avaliacao.py
Define a classe Avaliacao, com dois atributos:

_cliente: nome do cliente que avaliou.

_nota: nota da avaliação (de 1 a 5).

Essa classe é utilizada internamente pelo restaurante para armazenar as avaliações.


🔹 app.py
Ponto de entrada da aplicação. Aqui é criado um restaurante e inseridas algumas avaliações de exemplo.

restaurante_praça = Restaurante('Praça', 'Gourmet')
restaurante_praça.receber_avaliacao('Felipe', 10)  # Nota inválida (> 5), será ignorada
restaurante_praça.receber_avaliacao('Jorge', 5)
restaurante_praça.receber_avaliacao('Luana', 8)    # Também será ignorada (> 5)
restaurante_praça.receber_avaliacao('Pablo', 2)


Observação: Atualmente, o método receber_avaliacao só aceita notas entre 1 e 5. Notas fora desse intervalo são ignoradas. Considere validar ou ajustar esses valores para testes.


1. Como Executar
https://github.com/felipe7197/Sistema-avaliando-Restaurantes

2. Execute o projeto com:
python app.py


 Autor
Seu Nome – @felipe7197

