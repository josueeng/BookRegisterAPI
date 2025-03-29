# API de Gerenciamento de Livros

Esta é uma API desenvolvida em Python utilizando Flask para gerenciar um banco de dados de livros. A API permite cadastrar novos livros e listar os livros cadastrados.

## Funcionalidades

- **Cadastrar Livro**: Permite adicionar um novo livro ao banco de dados.
- **Listar Livros**: Retorna todos os livros cadastrados no banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web utilizado para criar a API.
- **SQLite**: Banco de dados utilizado para armazenar as informações dos livros.
- **Flask-CORS**: Biblioteca para habilitar CORS na API.

## Endpoints

### 1. Cadastrar Livro

- **URL**: `/doar`
- **Método**: `POST`
- **Descrição**: Cadastra um novo livro no banco de dados.
- **Corpo da Requisição (JSON)**:
    ```json
    {
        "titulo": "Título do Livro",
        "categoria": "Categoria do Livro",
        "autor": "Autor do Livro",
        "image_url": "URL da Imagem do Livro"
    }
    ```
- **Respostas**:
    - `201 Created`: Livro cadastrado com sucesso.
    - `400 Bad Request`: Todos os campos são obrigatórios.

### 2. Listar Livros

- **URL**: `/livros`
- **Método**: `GET`
- **Descrição**: Retorna uma lista de todos os livros cadastrados.
- **Resposta**:
    ```json
    [
        {
            "id": 1,
            "titulo": "Título do Livro",
            "categoria": "Categoria do Livro",
            "autor": "Autor do Livro",
            "image_url": "URL da Imagem do Livro"
        }
    ]
    ```

## Como Executar

1. Clone o repositório.
2. Instale as dependências listadas no arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
3. Execute o arquivo principal:
     ```bash
     python api.py
     ```
4. Acesse a API em `http://127.0.0.1:5000`.

## Dependências

As dependências necessárias estão listadas no arquivo `requirements.txt`:

```
blinker==1.9.0
click==8.1.8
colorama==0.4.6
Flask==3.1.0
flask-cors==5.0.1
gunicorn==23.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
packaging==24.2
Werkzeug==3.1.3
```

## Estrutura do Banco de Dados

A tabela `LIVROS` possui os seguintes campos:

- `id`: Identificador único do livro (INTEGER, PRIMARY KEY, AUTOINCREMENT).
- `titulo`: Título do livro (TEXT, NOT NULL).
- `categoria`: Categoria do livro (TEXT, NOT NULL).
- `autor`: Autor do livro (TEXT, NOT NULL).
- `image_url`: URL da imagem do livro (TEXT, NOT NULL).

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
