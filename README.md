# bluestorm_api
Projeto para Bluestorm relativo ao processo seletivo para a vaga de back-end da empresa. É uma API REST privada que fornece informações de compras dos pacientes/clientes para o setor financeiro de uma outra empresa da área da saúde.

# Endpoints disponíveis

`[POST]/auth` - endpoint onde uma autenticação é realizada. Uma requisição HTTP POST com método de autenticação Basic Auth precisa ser realizada para que o endpoint retorne dados com um token, uma mensagem e uma data de expiração desse token no formato JSON. Esse token deve ser utilizado em todas as outras requisições GET como parâmetro na URL para que dados válidos possam ser retornados ao usuário da API.  

`[GET]/patients` - endpoint onde são listadas as informações dos pacientes. Quando a autenticação é realizada de maneira correta, ele retorna dados no formato JSON com ID, nome, sobrenome e data de nascimento dos pacientes.

`[GET]/pharmacies` - endpoint onde são listadas as informações das farmácias. Quando a autenticação é realizada de maneira correta, ele retorna dados no formato JSON com ID, nome e cidade das farmácias.

`[GET]/transactions` - endpoint onde serão listadas as informações das transações realizadas entre os pacientes e as farmácias. Quando a autenticação é realizada de maneira correta, ele retorna dados no formato JSON com ID do paciente, nome do paciente, sobrenome do paciente, data de nascimento do paciente, ID da farmácia, nome da farmácia, cidade da farmácia, ID da transação, quantidade da transação e data da transação.

# Como executar a API localmente
Para executar a API localmente é necessário ter instalado:

- `Python 3`

Então clonar este repositório:

- `git clone https://github.com/rennesfreitassouza/projeto_bluestorm.git`

Navegar via linha de comando até o diretório criado após o download do repositório ser feito.

- `cd projeto_bluestorm/`

Criar um virtual environment [1], ativá-lo [2] para então instalar os módulos que são usados para executar o projeto [3].

- `python -m venv env` [1]

- `env\Scripts\activate` [2]

- `pip install -r requirements.txt` [3]

Instanciar a variável ambiente FLASK_APP com o valor válido:

- `set FLASK_APP=bluestorm_api`

Por fim, executar a API REST:

- `flask run`

# Como fazer requisições para a API
Para facilitar a interação com os endpoints do projeto, recomenda-se que o software Postman seja utilizado. Uma collection com o nome Bluestorm.postman_collection.json pronta para ser utilizada pelo Postman pode ser encontrada neste repositório e está disponível no diretório raíz. A seguir, uma breve explicação de como devem ser feitas as requisições para que dados válidos sejam retornados pela API REST privada.

`http://127.0.0.1:5000/auth` - uma requisição POST com Basic Auth precisa ser feita para que um token seja retornado por esse endpoint. O usuário `admin` e a senha `admin` já foram inseridos na tabela USERS do banco de dados bluestorm_api/backend_test.db para que a autenticação seja considerada válida e um token seja retornado para o usuário. Após realizar essa requisição, com esse tipo de autenticação e com esse usuário e senha, armazenar o token retornado para ser utilizado nas próximas requisições.

`http://127.0.0.1:5000/patients?token=` após o sinal de igual, inserir o token obtido da rota `http://127.0.0.1:5000/auth`. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de pacientes poderão ser obtidos.

`http://127.0.0.1:5000/pharmacies?token=` após o sinal de igual, inserir o token obtido da rota `http://127.0.0.1:5000/auth`. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de farmácias poderão ser obtidos.

`127.0.0.1:5000/transactions?token=` após o sinal de igual, inserir o token obtido da rota `http://127.0.0.1:5000/auth`. Assim, ao realizar uma requisição HTTP GET para esse endereço, dados válidos de transações poderão ser obtidos.

