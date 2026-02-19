<h1 align="center">BlackBank</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Pydantic-Validation-0A1A2F?style=for-the-badge" />
</p>

<hr>

<h2>📌 Sobre o Projeto</h2>

<p>
O <strong>BlackBank</strong> é um projeto backend desenvolvido com finalidade educacional, com o objetivo de consolidar conhecimentos em desenvolvimento de APIs REST com Python.
</p>

<p>
A proposta foi simular um sistema financeiro com funcionalidades abstratas semelhantes às de um banco, sem a intenção de reproduzir regras ou estruturas de instituições financeiras reais. O foco do projeto está na aplicação prática de conceitos de arquitetura, modelagem de dados, persistência e organização de código.
</p>

<hr>

<h2>🎯 Objetivo Técnico</h2>

<ul>
  <li>Construção de APIs REST com FastAPI</li>
  <li>Modelagem relacional com PostgreSQL</li>
  <li>Mapeamento ORM com SQLAlchemy</li>
  <li>Validação estrutural de dados com Pydantic</li>
  <li>Organização de projeto em camadas</li>
  <li>Registro de histórico e rastreabilidade de entidades</li>
</ul>

<hr>

<h2>🛠 Tecnologias Utilizadas</h2>

<ul>
  <li>Python</li>
  <li>FastAPI</li>
  <li>SQLAlchemy</li>
  <li>PostgreSQL</li>
  <li>Pydantic</li>
</ul>

<hr>

<h2>🧱 Arquitetura e Organização</h2>

<p>
O projeto foi estruturado de forma modular, com separação por responsabilidade em pastas distintas:
</p>

<ul>
  <li><strong>models</strong> — definição das entidades e mapeamento ORM</li>
  <li><strong>schemas</strong> — modelos de validação e serialização (Pydantic)</li>
  <li><strong>routes</strong> — definição dos endpoints</li>
  <li><strong>database</strong> — configuração de conexão e sessão</li>
  <li><strong>services</strong> — camada de lógica de negócio</li>
</ul>

<p>
Essa organização foi adotada com o objetivo de praticar separação de responsabilidades, legibilidade e escalabilidade da aplicação.
</p>

<hr>

<h2>📂 Estrutura de Domínio</h2>

<ul>
  <li><strong>Usuários</strong></li>
  <li><strong>Contas</strong></li>
  <li><strong>Transações</strong></li>
  <li><strong>Estados</strong> (histórico de alterações de contas)</li>
</ul>

<p>
Além do estado atual armazenado na conta, o projeto mantém um histórico de mudanças de estado com registro de data e hora, permitindo rastreabilidade das alterações.
</p>

<hr>

<h2>⚙️ Funcionalidades Implementadas</h2>

<ul>
  <li>Criação de usuários</li>
  <li>Criação de contas vinculadas a usuários</li>
  <li>Depósito</li>
  <li>Saque</li>
  <li>Transferência entre contas</li>
  <li>Registro persistente das operações</li>
  <li>Registro de data e hora de criação das entidades</li>
  <li>Histórico de mudança de estados de contas</li>
</ul>

<hr>

<h2>✅ Validação de Dados</h2>

<p>
O projeto implementa validação estrutural dos dados de entrada utilizando Pydantic, garantindo:
</p>

<ul>
  <li>Tipagem correta</li>
  <li>Formato adequado dos campos</li>
  <li>Regras básicas de obrigatoriedade</li>
</ul>

<p>
Não há validação de veracidade externa (ex: validação real de CPF), pois o objetivo foi focar na estrutura técnica da aplicação.
</p>

<hr>

<h2>🚀 Como Executar</h2>

<h3>1️⃣ Criar e ativar ambiente virtual</h3>

<pre><code>python -m venv venv
venv\Scripts\activate  # Windows</code></pre>

<h3>2️⃣ Instalar dependências</h3>

<pre><code>pip install -r requirements.txt</code></pre>

<h3>3️⃣ Configurar PostgreSQL local</h3>

<p>Exemplo de string de conexão:</p>

<pre><code>postgresql://postgres:postgres@localhost:5432/blackbank</code></pre>

<h3>4️⃣ Executar a aplicação</h3>

<pre><code>uvicorn app.main:app --reload</code></pre>

<p>Documentação interativa disponível em:</p>

<pre><code>http://127.0.0.1:8000/docs</code></pre>

<hr>

<h2>📎 Observações Finais</h2>

<ul>
  <li>O projeto não possui autenticação.</li>
  <li>Não foi desenvolvido com base em regras bancárias reais.</li>
  <li>O foco foi exclusivamente educacional e técnico.</li>
  <li>O principal objetivo foi praticar organização de código, modelagem de dados e construção de APIs estruturadas.</li>
</ul>

