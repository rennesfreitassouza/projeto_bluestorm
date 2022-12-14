# bluestorm_api
Projeto para Bluestorm relativo ao processo seletivo para a vaga de back-end da empresa. É uma API REST privada que fornece informações de compras dos pacientes/clientes para o setor financeiro de uma outra empresa da área da saúde.

# Endpoints disponíveis

`[POST]/auth` - Este endpoint realiza uma autenticação. Uma requisição HTTP POST com método de autenticação Basic Auth precisa ser realizada para que o endpoint retorne dados com um token, uma mensagem e uma data de expiração desse token no formato JSON. Esse token deve ser utilizado em todas as outras requisições GET como parâmetro na URL para que dados válidos possam ser retornados ao usuário da API.  

`[GET]/patients` - Aqui são listadas as informações dos pacientes. Quando a autenticação é realizada de maneira correta, ele retorna dados no formato JSON com ID, nome, sobrenome e data de nascimento dos pacientes.

`[GET]/pharmacies` - Neste são listadas as informações das farmácias. Quando a autenticação é realizada de maneira correta, ele retorna dados no formato JSON com ID, nome e cidade das farmácias.

`[GET]/transactions` - Endpoint onde serão listadas as informações das transações realizadas entre os pacientes e as farmácias. Se autenticada de maneira correta, ele retorna dados no formato JSON com ID do paciente, nome do paciente, sobrenome do paciente, data de nascimento do paciente, ID da farmácia, nome da farmácia, cidade da farmácia, ID da transação, quantidade da transação e data da transação.

# Como executar a API localmente
Para executar a API localmente é necessário ter instalado:

- `Python 3.x`

Então clonar este repositório:

- `git clone https://github.com/rennesfreitassouza/projeto_bluestorm.git`

Navegar via linha de comando até o diretório criado após o download do repositório ser feito.

- `cd projeto_bluestorm/`

Criar um virtual environment [1], ativá-lo [2] para então instalar os módulos que são usados para executar o projeto [3].

- `python -m venv env` [1]

- `env\Scripts\activate` [2] ou `source env/bin/activate` [2]

- `pip install -r requirements.txt` [3]

Instanciar a variável ambiente FLASK_APP com o valor válido:

- `set FLASK_APP=bluestorm_api` ou `export FLASK_APP=bluestorm_api`

Por fim, executar a API REST:

- `flask run`

# Como executar um container com a API
Para executar um container docker com a API é necessário ter instalado localmente o Docker (baixar em docker.com).

Para executar um container, comece executando o Docker (Docker daemon). Então, clone este repositório:

- `git clone https://github.com/rennesfreitassouza/projeto_bluestorm.git`

Navege via linha de comando até o diretório criado após o download do repositório ser feito.

- `cd projeto_bluestorm/`

Execute o comando a seguir como administrador para construir a imagem Docker e executar o container com a API:

- `docker-compose up -d --build`

Agora requisições já podem ser feitas para a API por meio do endereço 127.0.0.1, na porta 5000.

# Como fazer requisições para a API
Para facilitar a interação com os endpoints do projeto, recomenda-se que o software Postman seja utilizado. Uma collection com o nome `Bluestorm.postman_collection.json` pronta para ser utilizada pelo Postman pode ser encontrada no diretório raíz. A seguir, há uma breve explicação de como devem ser feitas as requisições para que dados válidos sejam retornados pela API REST privada.

- `http://127.0.0.1:5000/auth` - uma requisição POST com Basic Auth precisa ser feita para que um token seja retornado por esse endpoint. O usuário `admin` e a senha `admin` já foram inseridos na tabela USERS do banco de dados bluestorm_api/backend_test.db para que a autenticação seja considerada válida e um token seja retornado para o usuário. Após realizar essa requisição, com esse tipo de autenticação e com esse usuário e senha, armazenar o token retornado para ser utilizado nas próximas requisições.


- `http://127.0.0.1:5000/patients?token=` após o sinal de igual, inserir o token obtido da rota `http://127.0.0.1:5000/auth`. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de pacientes poderão ser obtidos.
  - Opcional: adicionar o parâmetro `first_name` para realizar a busca no endpoint `/patients` por meio do nome do paciente. O endereço ficará `http://127.0.0.1:5000/patients?token=&first_name=`. O valor para o nome do paciente procurado deve ser adicionado após `&first_name=`.


- `http://127.0.0.1:5000/pharmacies?token=` após o sinal de igual, inserir o token obtido da rota `http://127.0.0.1:5000/auth`. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de farmácias poderão ser obtidos.
  - Opcional: adicionar o parâmetro `name` para realizar a busca no endpoint `/pharmacies` por meio do nome da farmácia. O endereço ficará `http://127.0.0.1:5000/pharmacies?token=&name=`. O valor para o nome da farmácia procurada deve ser adicionado após `&name=`.


- `127.0.0.1:5000/transactions?token=` após o sinal de igual, inserir o token obtido da rota `http://127.0.0.1:5000/auth`. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de transações poderão ser obtidos.
  - Opcional: adicionar os parâmetros `pa_first_name` e `ph_name` para realizar a busca no endpoint `/transactions`, respectivamente por meio do nome do paciente e do nome da farmácia. O endereço ficará `http://127.0.0.1:5000/transactions?token=&pa_first_name=&ph_name=`. O valor para o nome do paciente procurado deve ser adicionado após `&pa_first_name=` e o valor para o nome da farmácia procurada deve ser adicionado após `&ph_name=`.

# Comandos via linha de comando
A REST API também permite que alguns comandos customizados sejam executados via linha de comando. Eles foram criados para facilitar no desenvolvimento do projeto e a utilização do serviço local.
- `flask endpoints` ou `docker-compose exec web flask endpoints` - Apresenta informações sobre os endpoints.

- `flask about` ou `docker-compose exec web flask about`- Apresenta informações sobre o autor do projeto.

- `flask adduser` ou `docker-compose exec web flask adduser` - Permite que dados de um novo usuário (username e passworld) sejam inseridos na tabela USERS para serem usados para obtenção de um token jwt. O comando também aceita parâmetros opcionais. Por exemplo, o comando `flask adduser --user admin --password teste_@dmin` ou `docker-compose exec web flask adduser --user admin --password teste_@dmin` adiciona o usuário admin com senha teste_@dmin na tabela USERS.

- `flask removeuser` ou `docker-compose exec web flask removeuser` - Permite que dados de um usuário (username e passworld) sejam removidos da tabela USERS. O comando também aceita parâmetros opcionais. Por exemplo, o comando `flask removeuser --user admin --password teste_@dmin` ou `docker-compose exec web flask removeuser --user admin --password teste_@dmin` remove o usuário admin com senha teste_@dmin da tabela USERS.


# Como executar os casos de teste:
Uma das formas de executar os casos de teste é executar o pytest no diretório raiz com `pytest -vv` ou via docker compose `docker-compose exec web pytest` ou mesmo analisando [a saída com nome Test de uma das instruções de teste executada no GitHub Actions](https://github.com/rennesfreitassouza/projeto_bluestorm/runs/8288337881?check_suite_focus=true). Diversos casos de teste foram desenvolvidos para o código da API e cobrem 94% [(observar saída Coverage do GitHub Actions)](https://github.com/rennesfreitassouza/projeto_bluestorm/runs/8288337881?check_suite_focus=true) de todo o código que foi desenvolvido para o projeto. Alguns comandos úteis:

- `coverage run -m pytest` ou `docker-compose exec web coverage run -m pytest` para medir a cobertura de código realizada pelos casos de teste.

- `coverage report` ou  `docker-compose exec web coverage report` para ver o relatório de cobertura via linha de comando.

# Considerações finais
Para garantir que o código do projeto se adequasse aos padrões e estilo sugeridos pela comunidade, foi utilizado o [Pylint](https://github.com/PyCQA/pylint). Também gostaria de agradecer a [empresa Bluestorm](https://www.bluestorm.com.br/) pelo gratificante desafio.
