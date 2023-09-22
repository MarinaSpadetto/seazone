# Desafio Seazone Backend

Esta aplicação foi desenvolvida para o criar e gerenciar um banco de dados com três entidades principais: Imóveis, Anúncios e Reservas. Neste README, você encontrará informações essenciais sobre como configurar e executar este projeto.

## Descrição

A Empresa Khanto iniciou o desenvolvimento de um novo sistema que visa atender às necessidades de gerenciamento de informações relacionadas a imóveis, anúncios e reservas. Abaixo estão as principais características do sistema:

### Estrutura do Banco de Dados

![DBML Khanto](/static/dbml.png)

- **Property**: Um property(imóvel) pode ter vários anúncios associados a ele.

- **Advertisement**: Cada advertisement(anúncio) está vinculado a um property específico. E um advertisement pode ter várias reservas.

- **Reservation**: Uma reservation(reserva) é referente a um advertisement específico.

Este sistema permite que a Empresa Khanto gerencie eficientemente suas operações relacionadas a imóveis, anúncios e reservas, fornecendo uma plataforma centralizada para registrar e consultar informações.

## Documentação da API

Para visualizar a documentação da API:

   - http://localhost:8000/swagger/ - [Acesse](https://swagger.io/tools/swagger-ui/) para mais informações sobre `swagger-ui`.
   - http://localhost:8000/redoc/ - [Acesse](https://github.com/Redocly/redoc) para mais informações sobre `redoc`.

Certifique-se de efetuar o login antes de acessar a documentação.

## Configurações do Projeto

Esta aplicação pode ser executada em diferentes ambientes.

### Configuração e Execução com Ambiente Virtual (env)

Para executar a aplicação usando um ambiente virtual (env), siga estas etapas:

1. Clone este repositório em sua máquina local:

   ```
   git clone https://github.com/MarinaSpadetto/seazone.git
   ```

2. Crie um ambiente virtual usando venv ou virtualenv:

   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   No Windows:
    ```
    venv\Scripts\activate
    ```

   No macOS e Linux:
    ```
    source venv/bin/activate
    ```

4. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:

   ```
   python manage.py migrate
   ```

6. Crie um usuário:

   ```
   python manage.py createsuperuser
   ```
   
7. Execute a fixture:

   ```
   python manage.py loaddata khanto/fixtures/initial_data.json
   ```

8. Inicie o servidor de desenvolvimento:

   ```
   python manage.py runserver
   ```

A aplicação agora estará em execução em http://localhost:8000/.

### Configuração e Execução com Docker Compose

Para executar a aplicação usando Docker Compose, siga estas etapas:

1. Clone este repositório em sua máquina local:

   ```
   git clone https://github.com/MarinaSpadetto/seazone.git
   ```

2. Acesse o diretório da aplicação:

   ```
   cd seazone
   ```

3. Construa e inicie os contêineres Docker usando Docker Compose:

    ```
    docker-compose up -d --build
    ```

A aplicação agora estará em execução em http://localhost:8000/.


### Observações

1. Lembre-se de parar os contêineres Docker (usando `docker-compose down`) ou desativar o ambiente virtual (usando `deactivate`) quando não estiver usando a aplicação.
2. A escolha entre o uso de um ambiente virtual ou Docker Compose depende da preferências da equipe.
