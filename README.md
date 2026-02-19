BlackBank
📌 Sobre o Projeto

O BlackBank é um projeto backend desenvolvido com finalidade educacional, com o objetivo de consolidar conhecimentos em desenvolvimento de APIs REST com Python.

A proposta foi simular um sistema financeiro com funcionalidades abstratas semelhantes às de um banco, sem a intenção de reproduzir regras ou estruturas de instituições financeiras reais. O foco do projeto está na aplicação prática de conceitos de arquitetura, modelagem de dados, persistência e organização de código.

🎯 Objetivo Técnico

Praticar e consolidar:

Construção de APIs REST com FastAPI

Modelagem relacional com PostgreSQL

Mapeamento ORM com SQLAlchemy

Validação estrutural de dados com Pydantic

Organização de projeto em camadas

Registro de histórico e rastreabilidade de entidades

🛠 Tecnologias Utilizadas

Python

FastAPI

SQLAlchemy

PostgreSQL

Pydantic

🧱 Arquitetura e Organização

O projeto foi estruturado de forma modular, com separação por responsabilidade em pastas distintas, como por exemplo:

models — definição das entidades e mapeamento ORM

schemas — modelos de validação e serialização (Pydantic)

routers — definição dos endpoints

database — configuração de conexão e sessão

services ou camada lógica (quando aplicável)

Essa organização foi adotada com o objetivo de praticar separação de responsabilidades, legibilidade e escalabilidade da aplicação.

📂 Estrutura de Domínio

O sistema é composto pelas seguintes entidades principais:

Usuários

Contas

Transações

Estados (histórico de alterações de contas)

Além do estado atual armazenado na conta, o projeto mantém um histórico de mudanças de estado com registro de data e hora, permitindo rastreabilidade das alterações.

⚙️ Funcionalidades Implementadas

Criação de usuários

Criação de contas vinculadas a usuários

Depósito

Saque

Transferência entre contas

Registro persistente das operações

Registro de data e hora de criação das entidades

Histórico de mudança de estados de contas

✅ Validação de Dados

O projeto implementa validação estrutural dos dados de entrada utilizando Pydantic, garantindo:

Tipagem correta

Formato adequado dos campos

Regras básicas de obrigatoriedade

Não há validação de veracidade externa (ex: validação real de CPF), pois o objetivo foi focar na estrutura técnica da aplicação.

🚀 Como Executar
1. Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
2. Instalar dependências
pip install -r requirements.txt
3. Configurar PostgreSQL local

O projeto utiliza PostgreSQL rodando localmente.

Exemplo de conexão:

postgresql://postgres:postgres@localhost:5432/blackbank
4. Executar a aplicação
uvicorn app.main:app --reload

Documentação interativa disponível em:

http://127.0.0.1:8000/docs
📎 Observações Finais

O projeto não possui autenticação.

Não foi desenvolvido com base em regras bancárias reais.

O foco foi exclusivamente educacional e técnico.

O principal objetivo foi praticar organização de código, modelagem de dados e construção de APIs estruturadas.