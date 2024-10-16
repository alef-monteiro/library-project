### Library Management System API

#### Descrição
API simples para gerenciar uma biblioteca, permitindo operações de CRUD (Create, Read, Update, Delete) para bibliotecários, clientes, livros, autores, gêneros e empréstimos.

#### Funcionalidades
- CRUD completo para:
  - Bibliotecários (Librarian)
  - Clientes (Clients)
  - Livros (Books)
  - Autores (Authors)
  - Gêneros de livros (Genres)
  - Empréstimos (Loans)
  
- Listagens que incluem:
  - ID
  - Data de criação
  - Data de modificação
  - Status ativo/inativo

#### Tecnologias
- Django
- PostgreSQL
- Dependências listadas em `requirements.txt`

#### Instalação
1. Clone o repositório:
   - git clone https://github.com/alef-monteiro/library-project.git
   - cd library-project

2. Instale as dependências:
   - pip install -r requirements.txt

3. Configure o banco de dados no arquivo `library.config`:
    DB_ENGINE=django.db.backends.postgresql_psycopg2
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=library
    DB_USER=postgres
    DB_PASS=123456

4. Realize as migrações:
   - python manage.py makemigrations
   depois:
   - python manage.py migrate

6. Inicie o servidor:
   - python manage.py runserver

### Estrutura das Entidades

- **Clients**: id, name, cpf, age, favourite_genre, created_at, updated_at, is_active
- **Books**: id, title, author, genre, number_pages, available_copies, created_at, updated_at, is_active
- **Authors**: id, name, created_at, updated_at, is_active
- **Genres**: id, name, created_at, updated_at, is_active
- **Loans**: id, id_client, id_book, loan_day, return_day, created_at, updated_at, is_active

#### Endpoints
- `/basic-library/clients/`
- `/basic-library/books/`
- `/basic-library/authors/`
- `/basic-library/genres/`
- `/basic-library/loans/`

#### Autor
- [Seu Nome] – [seu-email@exemplo.com]

---

Com isso, você deve ter um README mais claro e organizado, sem o uso de caixas pretas. Se precisar de mais alguma coisa, é só avisar!
